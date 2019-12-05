#!/usr/bin/python
# coding=utf8
# author: Sun yang


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipviewsip.settings')
import django
import pickle
import re
django.setup()
from ipdata import models
import sys
import datetime

dic = {}
# {"事业部"：{项目：{service:[内存总量，内存使用量, 内存使用率，硬盘总量,硬盘使用量,硬盘使用率],bigdata:[内存总量，内存使用量, 内存使用率，硬盘总量,硬盘使用量,硬盘使用率]}}}
all_dic = {}
error_list = []



def create_dic():
    ip = models.IpConfig.objects.all().prefetch_related('env')
    for i in ip:
        dic.setdefault(i.env.to_b.name, {})
        all_dic.setdefault(i.env.to_b.name, {})
        all_dic[i.env.to_b.name].setdefault(i.env.name,{})
        dic[i.env.to_b.name].setdefault(i.env.name, {})
        all_dic[i.env.to_b.name][i.env.name].setdefault("bigdata", [0,0,0,0,0,0])
        all_dic[i.env.to_b.name][i.env.name].setdefault("service", [0,0,0,0,0,0])
        dic[i.env.to_b.name][i.env.name].setdefault("bigdata", [])
        dic[i.env.to_b.name][i.env.name].setdefault("server", [])
        if i.type == 0:
            dic[i.env.to_b.name][i.env.name]["server"].append(i.ip)
        else:
            dic[i.env.to_b.name][i.env.name]["bigdata"].append(i.ip)


# 创建基础数据表
create_dic()

# 读取pickle
salt_6 = open('10.10.7.6.pkl', 'rb')
salt_1 = open('10.11.8.1.pkl', 'rb')

p_6 = pickle.load(salt_6, encoding="utf-8")
p_1 = pickle.load(salt_1, encoding="utf-8")

# 记录失败ip
error_list.extend(p_6[0])
error_list.extend(p_1[0])

print(error_list)


#sys.exit()


def insert_db(pk,status=True):
    r = re.compile(r"[\d\.]+")
    time_obj = models.RecordingTime.objects.filter().last()
    now_n = datetime.datetime.now()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    if time_obj:
        if str(time_obj.pub_date) == now:
            time_id = time_obj.id
        else:
            time_id = models.RecordingTime.objects.create(pub_date=now_n).id

    else:
        time_id = models.RecordingTime.objects.create(pub_date=now_n).id
    # return True
    for i in pk[1:]:
        for k, v in i.items():
            try:
                host_l = v['ret']['stdout'].split("|")  # 获取每台主机的信息
            except TypeError as f:
                print(f,v)
                continue
            config_obj = models.IpConfig.objects.filter(ip=host_l[0])
            if config_obj:
                env_id = config_obj[0].env.id
                config_type = config_obj[0].type
                env_name = config_obj[0].env.name
                b_name = config_obj[0].env.to_b.name
                default1 = {"memorytotal": host_l[1], "memoryuse": host_l[2], "memoryrate": r.findall(host_l[3])[0],"cpurate":host_l[10],
                           "cpucore": host_l[4], "averageload": 0 if host_l[5]=="" else host_l[5], "disktotal": host_l[6], "diskuse": host_l[7],
                           "diskrate": r.findall(host_l[8])[0], "servertype": 1, "env_id": env_id,"type":config_type}
                default2 = {"memorytotal": host_l[1], "memoryuse": host_l[2], "memoryrate": r.findall(host_l[3])[0],"cpurate":host_l[10],
                           "cpucore": host_l[4], "averageload": 0 if host_l[5]=="" else host_l[5], "disktotal": host_l[6], "diskuse": host_l[7],
                           "diskrate": r.findall(host_l[8])[0], "servertype": 0, "env_id": env_id,"type":config_type}
                if status:
                    if host_l[9] == "物理机":
                        models.IpInfo.objects.update_or_create(name=host_l[0],times_id=time_id,defaults=default1)
                        config_obj.update(servertype=1)
                    else:
                        models.IpInfo.objects.update_or_create(name=host_l[0],times_id=time_id,defaults=default2)
                        config_obj.update(servertype=0)
                if config_type == 0:
                    all_dic[b_name][env_name]["service"][0] += int(host_l[1])
                    all_dic[b_name][env_name]["service"][1] += int(host_l[2])

                    all_dic[b_name][env_name]["service"][3] += float(host_l[6])
                    all_dic[b_name][env_name]["service"][4] += float(host_l[7])

                else:
                    all_dic[b_name][env_name]["bigdata"][0] += int(host_l[1])
                    all_dic[b_name][env_name]["bigdata"][1] += int(host_l[2])
                    all_dic[b_name][env_name]["bigdata"][3] += float(host_l[6])
                    all_dic[b_name][env_name]["bigdata"][4] += float(host_l[7])

            else:
                # 在IpConfig 表内没有的服务器
                print("db tables is not ip:%s" % host_l[0])


# 插入IpInfo 表数据
insert_db(p_6)
insert_db(p_1)

# 不插入只计算
# insert_db(p_6,status=False)
# insert_db(p_1,status=False)

def all_dic_rate():
    for k,v in all_dic.items():
        for kk,vv in v.items():
            if vv["service"][0] != 0:
                use_rate = vv["service"][1]/vv["service"][0]*100
                vv["service"][2] = use_rate
                use_rate = vv["service"][4]/vv["service"][3]*100
                vv["service"][5] = use_rate
            if vv["bigdata"][0] != 0:
                use_rate = vv["bigdata"][1]/vv["bigdata"][0]*100
                vv["bigdata"][2] = use_rate
                use_rate = vv["bigdata"][4]/vv["bigdata"][3]*100
                vv["bigdata"][5] = use_rate

def insert_all():
    time_obj = models.RecordingTime.objects.filter().last()
    now_n = datetime.datetime.now()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    if time_obj:
        if str(time_obj.pub_date) == now:
            time_id = time_obj.id
        else:
            time_id = models.RecordingTime.objects.create(pub_date=now_n).id

    else:
        time_id = models.RecordingTime.objects.create(pub_date=now_n).id

    for k,v in all_dic.items():
        for kk,vv in v.items():
            e_obj = models.Environment.objects.get(name=kk,to_b__name=k)
            if vv["service"][0] != 0:
                models.AllData.objects.update_or_create(env_id=e_obj.id, time_id=time_id, type=0,defaults={
                    "type":0,"memorytotal":vv["service"][0],"memoryuse":vv["service"][1],"memoryrate":float("%0.2f"%vv["service"][2]),
                    "disktotal":vv["service"][3],"diskuse":vv["service"][4],"diskrate":float("%0.2f"%vv["service"][5])
                })

            if vv["bigdata"][0] != 0:
                models.AllData.objects.update_or_create(env_id=e_obj.id, time_id=time_id, type=1,defaults={
                    "type":1,"memorytotal":vv["bigdata"][0],"memoryuse":vv["bigdata"][1],"memoryrate":float("%0.2f"%vv["bigdata"][2]),
                    "disktotal":vv["bigdata"][3],"diskuse":vv["bigdata"][4],"diskrate":float("%0.2f"%vv["bigdata"][5])
                })






# 计算各个项目的总量
all_dic_rate()

# 插入AllData 表的数据
insert_all()
