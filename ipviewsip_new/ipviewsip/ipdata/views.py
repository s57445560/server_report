from django.shortcuts import render

# Create your views here.

from rest_framework.pagination import PageNumberPagination
from ipdata import models
from .models import BusinessUnit,IpInfo,Environment,RecordingTime,AllData
import datetime
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
from openpyxl.styles.colors import GREEN, BLACK
from django.http import FileResponse
import os



class UsersSerializer(serializers.ModelSerializer):
    environment_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.BusinessUnit
        fields = "__all__"				# 查询表内所有的内容
        depth = 2					# 设置连表的深度，如果被连表还有连表 可以设置为2


class IpinfoSerializer(serializers.ModelSerializer):
    times = serializers.StringRelatedField(label='时间')
    servertype = serializers.CharField(source="get_servertype_display")
    type = serializers.CharField(source="get_type_display")
    class Meta:
        model = IpInfo
        fields = "__all__"				# 查询表内所有的内容


class AlldataSerializer(serializers.ModelSerializer):

    time = serializers.StringRelatedField(label='时间')
    class Meta:
        model = AllData
        fields = "__all__"				# 查询表内所有的内容



class Base_info(APIView):
    def get(self,request,*args,**kwargs):
        ret = models.BusinessUnit.objects.all()
        ser = UsersSerializer(instance=ret,many=True)		# many 是否是多条数据，如果单条使用False
        for k in ser.data:
            for i in k["environment_set"]:
                k.setdefault("e_list",[])
                k['e_list'].append(i.split("|"))
        return Response(ser.data)		# ensure_ascii json时显示中文


class StandartPageNumberPagination(PageNumberPagination):
    page_size = 10 #默认每⻚返回的条数
    max_page_size = 20 #每⻚返回的最⼤条数
    page_size_query_param = 'page_size' #url中设置 page_size的键,默认为page_size
    page_query_param = 'page' #url中设置 page的键,默认为page

class Ip_info(APIView):
    def get(self,request,*args,**kwargs):
        env_name = request.GET.get("e")
        bus_name = request.GET.get("b")
        order = request.GET.get("order")
        filter_web = request.GET.get("filter")
        if not order:
            order = 'id'
        if not filter_web:
            filter_web = ''

        print(env_name, bus_name, order,filter_web)
        times = request.GET.get('timestrap')
        if not times:
            times = datetime.datetime.now().strftime("%Y-%m-%d")
        bus = Environment.objects.get(name=env_name, to_b__name=bus_name)
        if order == 'id':
            ips = IpInfo.objects.filter(env=bus, times__pub_date=times,name__contains=filter_web).order_by(order)
        else:
            ips = IpInfo.objects.filter(env=bus, times__pub_date=times,name__contains=filter_web).extra(select={'num':order+"+0"})
            ips = ips.extra(order_by=["num"])
        # 分页
        pg = StandartPageNumberPagination()
        pg_ips = pg.paginate_queryset(queryset=ips, request=request, view=self)
        ipser = IpinfoSerializer(instance=pg_ips, many=True)

        totalcount = IpInfo.objects.filter(env=bus,times__pub_date=times).count()
        vircount = IpInfo.objects.filter(env=bus,times__pub_date=times,type=0).count()
        ip_dict = {
            "servertotalcount":totalcount,"vircount":vircount,"phycount":totalcount-vircount,
            'select_number':ips.count(),
            "IP":ipser.data
        }
        return Response(ip_dict)


class All_info(APIView):

    def get(self,request,*args,**kwargs):

        env_name = request.GET.get("e")
        bus_name = request.GET.get("b")
        envobj = Environment.objects.get(name=env_name, to_b__name=bus_name)
        print(env_name,bus_name,"all")
        timestrap = request.GET.get('timestrap')
        if not timestrap:
            timestrap = datetime.datetime.now().strftime("%Y-%m-%d")
        busobj = BusinessUnit.objects.get(id=envobj.to_b_id)
        # timobj = RecordingTime.objects.get(pub_date=timestrap)
        alldata = AllData.objects.filter(env=envobj,time__pub_date=timestrap)
        alldataser = AlldataSerializer(instance=alldata,many=True)
        service = {
            'memorytotal': 0,
            'memoryuse': 0,
            'memoryrate': 0,
            'disktotal': 0,
            'diskuse': 0,
            'diskrate': 0
        }
        dic = {}
        for i in alldataser.data:
            if i['type'] == 0:
                dic['service'] = i
            else:
                dic['bigdata'] = i

        dic.setdefault('service', service)
        dic.setdefault('bigdata', service)
        all_dict = {

            'time': timestrap,
            'business': busobj.name,
            'all': dic,

        }
        return Response(all_dict)

class Home(APIView):
    def get(self,request,*args,**kwargs):
        dic = {}
        ip_all = models.IpConfig.objects.all().count()
        e_all = models.Environment.objects.all().count()
        b_obj = models.BusinessUnit.objects.all()
        dic = {
            'ip_all':ip_all,
            'e_all':e_all,
            'number':{},
            'b_list':[],
            'b_n_list':[]

        }
        for i in b_obj:
            number = models.IpConfig.objects.filter(env__to_b_id=i.id).count()
            name = i.name
            dic['number'][name] = number
            dic['b_list'].append(name)
            dic['b_n_list'].append(number)
        print(dic)
        return Response(dic)




from django.http import FileResponse

class Download(APIView):
    def get(self, request,*args,**kwargs):

        timestrap = request.GET.get("timestrap")
        head_data = ['序号','IP地址','内存总量/M','内存使用量/M','内存使用率','cpu核数','平均load值','磁盘总量/G','磁盘使用量/G','磁盘使用率','服务器类型']

        alldict = {}
        ips = None
        if timestrap:
            ips = IpInfo.objects.filter(times__pub_date=timestrap)
        else:
            ips = IpInfo.objects.filter(times__pub_date=datetime.datetime.now().strftime('%Y-%m-%d'))

        if not ips:
            print("status: False")
            return Response({"status":False})


        for j in ips:
            e = j.env.name
            b = j.env.to_b.name
            alldict.setdefault(b,{})
            alldict[b].setdefault(e,[])

            alldict[b][e].append([len(alldict[b][e])+1,j.name,j.memorytotal,j.memoryuse,j.memoryrate+'%',
                                 j.cpucore,str(j.averageload),float(j.disktotal),float(j.diskuse),
                                  j.diskrate+'%',j.get_servertype_display()])
        # 样式设置
        alignment = Alignment(horizontal='center', vertical='center')
        thin = Side(border_style="thin", color=BLACK)
        border = Border(top=thin, left=thin, right=thin, bottom=thin)
        row_title_font = Font(name='宋体', size=14, bold=True, color=BLACK)
        row_title_fill = PatternFill(fill_type='solid', fgColor='AACF91')
        content_font = Font(name='宋体', size=12, bold=False, color=BLACK)
        content_fill = PatternFill(fill_type='solid', fgColor='AACF91')
        title_font = Font(name="黑体", bold=True, size=16,color=BLACK)

        wb = Workbook()
        sheet = wb.active
        status = True

        for k1,v1 in alldict.items():
            if status:
                sheet.title = k1
                status = False
            else:
                sheet = wb.create_sheet(k1)
            num = 1
            for k2,v2 in v1.items():

                sheet.merge_cells(start_row=num, start_column=1, end_row=num, end_column=11)
                sheet.cell(num, 1).value = k2
                sheet.cell(num, 1).alignment = alignment
                sheet.cell(num, 1).font = title_font
                sheet.cell(num, 1).fill = row_title_fill
                num += 1
                sheet.append(head_data)
                rw = sheet.max_row
                sheet.column_dimensions['A'].width = 15
                sheet.column_dimensions['B'].width = 20
                sheet.column_dimensions['C'].width = 20
                sheet.column_dimensions['D'].width = 20
                sheet.column_dimensions['E'].width = 20
                sheet.column_dimensions['F'].width = 15
                sheet.column_dimensions['G'].width = 20
                sheet.column_dimensions['H'].width = 20
                sheet.column_dimensions['I'].width = 20
                sheet.column_dimensions['J'].width = 15
                sheet.column_dimensions['K'].width = 15
                sheet['A'+str(rw)].alignment = alignment
                sheet['A'+str(rw)].font = row_title_font
                sheet['B'+str(rw)].alignment = alignment
                sheet['B'+str(rw)].font = row_title_font
                sheet['C'+str(rw)].alignment = alignment
                sheet['C'+str(rw)].font = row_title_font
                sheet['D'+str(rw)].alignment = alignment
                sheet['D'+str(rw)].font = row_title_font
                sheet['E'+str(rw)].alignment = alignment
                sheet['E'+str(rw)].font = row_title_font
                sheet['F'+str(rw)].alignment = alignment
                sheet['F'+str(rw)].font = row_title_font
                sheet['G'+str(rw)].alignment = alignment
                sheet['G'+str(rw)].font = row_title_font
                sheet['H'+str(rw)].alignment = alignment
                sheet['H'+str(rw)].font = row_title_font
                sheet['I'+str(rw)].alignment = alignment
                sheet['I'+str(rw)].font = row_title_font
                sheet['J'+str(rw)].alignment = alignment
                sheet['J'+str(rw)].font = row_title_font
                sheet['K'+str(rw)].alignment = alignment
                sheet['K'+str(rw)].font = row_title_font


                num += 1
                vmnum = 0
                phnum = 0
                memtotal = 0
                memuse = 0
                disktotal = 0.0
                diskuse = 0.0
                for line in v2:
                    sheet.append(line)
                    memtotal += line[2]
                    memuse += line[3]
                    disktotal += line[7]
                    diskuse += line[8]
                    if '虚拟机' in line:
                        vmnum += 1
                    else:
                        phnum += 1
                    darw = sheet.max_row
                    sheet['A' + str(darw)].alignment = alignment
                    sheet['A' + str(darw)].font = content_font
                    sheet['B' + str(darw)].alignment = alignment
                    sheet['B' + str(darw)].font = content_font
                    sheet['C' + str(darw)].alignment = alignment
                    sheet['C' + str(darw)].font = content_font
                    sheet['D' + str(darw)].alignment = alignment
                    sheet['D' + str(darw)].font = content_font
                    sheet['E' + str(darw)].alignment = alignment
                    sheet['E' + str(darw)].font = content_font
                    sheet['F' + str(darw)].alignment = alignment
                    sheet['F' + str(darw)].font = content_font
                    sheet['G' + str(darw)].alignment = alignment
                    sheet['G' + str(darw)].font = content_font
                    sheet['H' + str(darw)].alignment = alignment
                    sheet['H' + str(darw)].font = content_font
                    sheet['I' + str(darw)].alignment = alignment
                    sheet['I' + str(darw)].font = content_font
                    sheet['J' + str(darw)].alignment = alignment
                    sheet['J' + str(darw)].font = content_font
                    sheet['K' + str(darw)].alignment = alignment
                    sheet['K' + str(darw)].font = content_font
                    num += 1
                endrw = sheet.max_row

                # sheet.cell(row = endrw+1, column = 3).value = '=SUM(C'+str(rw+1)+':'+'C'+str(endrw)+')'
                sheet.cell(row = endrw+1, column = 3).value = memtotal
                sheet['C'+str(endrw+1)].font = content_font
                sheet['C'+str(endrw+1)].alignment = alignment

                # sheet.cell(row = endrw+1, column = 4).value = '=SUM(D'+str(rw+1)+':'+'D'+str(endrw)+')'
                sheet.cell(row = endrw+1, column = 4).value = memuse
                sheet['D' + str(endrw+1)].font = content_font
                sheet['D' + str(endrw+1)].alignment = alignment

                # sheet.cell(row = endrw+1, column = 8).value = '=SUM(H'+str(rw+1)+':'+'H'+str(endrw)+')'
                sheet.cell(row = endrw+1, column = 8).value = disktotal
                sheet['H' + str(endrw+1)].font = content_font
                sheet['H' + str(endrw+1)].alignment = alignment

                # sheet.cell(row = endrw+1, column = 9).value = '=SUM(I'+str(rw+1)+':'+'I'+str(endrw)+')'
                sheet.cell(row = endrw+1, column = 9).value = diskuse
                sheet['I' + str(endrw+1)].font = content_font
                sheet['I' + str(endrw+1)].alignment = alignment

                # 物理机 虚拟机    =COUNTIF(K2:K14,"虚拟机")
                # vmnum = '=COUNTIF(K' + str(rw + 1) + ':' + 'K' + str(endrw) +','+'"虚拟机"'+ ')'
                # phnum = '=COUNTIF(K' + str(rw + 1) + ':' + 'K' + str(endrw) +','+'"物理机"'+ ')'
                sheet.cell(row=endrw + 1, column=11).value = str(vmnum) +'/'+ str(phnum)
                sheet['K' + str(endrw + 1)].font = content_font
                sheet['K' + str(endrw + 1)].alignment = alignment


                num += 1
                sheet.cell(row=endrw + 2, column=3).value = '内存总量/M'
                sheet['C' + str(endrw+2)].font = content_font
                sheet['C' + str(endrw+2)].alignment = alignment
                sheet['C' + str(endrw+2)].fill = content_fill

                sheet.cell(row=endrw + 2, column=4).value = '内存使用总量/M'
                sheet['D' + str(endrw+2)].font = content_font
                sheet['D' + str(endrw+2)].alignment = alignment
                sheet['D' + str(endrw+2)].fill = content_fill

                sheet.cell(row=endrw + 2, column=8).value = '硬盘总量/G'
                sheet['H' + str(endrw+2)].font = content_font
                sheet['H' + str(endrw+2)].alignment = alignment
                sheet['H' + str(endrw+2)].fill = content_fill

                sheet.cell(row=endrw + 2, column=9).value = '硬盘使用总量/G'
                sheet['I' + str(endrw+2)].font = content_font
                sheet['I' + str(endrw+2)].alignment = alignment
                sheet['I' + str(endrw+2)].fill = content_fill

                sheet.cell(row=endrw + 2, column=11).value = '虚拟机/物理机'
                sheet['K' + str(endrw + 2)].font = content_font
                sheet['K' + str(endrw + 2)].alignment = alignment
                sheet['K' + str(endrw + 2)].fill = content_fill

                num += 1
                sheet.append([])
                num += 1

        wb.save('ipdatas.xlsx')
        paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = open(os.path.join(paths, 'ipdatas.xlsx'), 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="ipdatas.xlsx"'

        return response
