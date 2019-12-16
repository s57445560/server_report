#!/usr/bin/python
# coding=utf8
# author: Sun yang


import os
import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipviewsip.settings')
import django
import pickle
import re
import sys
django.setup()
from ipdata import models
import datetime
import requests
requests.packages.urllib3.disable_warnings()					# 让requests模块不报警告

# {"事业部"：{项目：{service:[内存总量，内存使用量, 内存使用率，硬盘总量,硬盘使用量,硬盘使用率],bigdata:[内存总量，内存使用量, 内存使用率，硬盘总量,硬盘使用量,硬盘使用率]}}}
all_dic = {}
error_list = []
ok_list = []



def create_dic():
    ip = models.IpConfig.objects.all().prefetch_related('env')
    for i in ip:
        all_dic.setdefault(i.env.to_b.name, {})
        all_dic[i.env.to_b.name].setdefault(i.env.name,{})
        all_dic[i.env.to_b.name][i.env.name].setdefault("bigdata", [0,0,0,0,0,0,0,0])
        all_dic[i.env.to_b.name][i.env.name].setdefault("service", [0,0,0,0,0,0,0,0])


class SaltApi(object):
    def __init__(self, ip, user, password):
        self.ip = ip
        self.url = 'https://%s/'%self.ip
        self.user = user
        self.headers = {'Accept': 'application/json',}
        self.password = password
        self.token_id = self.salt_login()
        self.headers['X-Auth-Token'] = self.token_id


    def salt_login(self):					# 登陆获取token
        params = {'eauth': 'pam', 'username': self.user, 'password': self.password}
        j = requests.post(url = self.url+"login", data=params,headers=self.headers,verify=False)
        return j.json()['return'][0]['token']


    def cmd(self,j):						# 执行同步的命令
        result = requests.post(url=self.url, data=j, headers=self.headers, verify=False)
        return result.json()["return"]


    def cmd_async(self,j):					# 异步执行命令
        result = requests.post(url=self.url, data=j, headers=self.headers, verify=False)
        print(result.json())
        return result.json()['return'][0]['jid']

    def look_jid(self,jid):					# 查看异步的命令需要jid
        params = {'client': 'runner', 'fun': 'jobs.lookup_jid', 'jid': jid}
        result = requests.post(url=self.url, data=params, headers=self.headers, verify=False)
        print(result.json())

    def all_list(self):						# 查看所有salt内的minion
        params = {'client': 'wheel', 'fun': 'key.list_all'}
        result = requests.post(url=self.url, data=params, headers=self.headers, verify=False)
        return result.json()['return'][0]['data']['return']['minions']




def insert_db(pk,status=True):
    r = re.compile(r"[\d\.]+")
    time_obj = models.RecordingTime.objects.filter().last()
    now_n = datetime.datetime.now()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    if time_obj:
        if str(time_obj.pub_date) == now:
            time_id = time_obj.id
        else:
            print("新建")
            time_id = models.RecordingTime.objects.create(pub_date=now_n).id

    else:
        time_id = models.RecordingTime.objects.create(pub_date=now_n).id
    # return True
    for i in pk:
        for k, v in i.items():
            try:
                host_l = v['stdout'].split("|")  # 获取每台主机的信息
            except TypeError as f:
                print(f,v)
                continue
            ok_list.append(k)
            config_obj = models.IpConfig.objects.filter(ip=host_l[0])
            if v["stderr"] != '':
                print("有错误的: ",v)
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

                    all_dic[b_name][env_name]["service"][6] += float(0.00 if host_l[10] == "" else host_l[10])
                    all_dic[b_name][env_name]["service"][7] += 1

                else:
                    all_dic[b_name][env_name]["bigdata"][0] += int(host_l[1])
                    all_dic[b_name][env_name]["bigdata"][1] += int(host_l[2])
                    all_dic[b_name][env_name]["bigdata"][3] += float(host_l[6])
                    all_dic[b_name][env_name]["bigdata"][4] += float(host_l[7])

                    all_dic[b_name][env_name]["bigdata"][6] += float(0.00 if host_l[10] == "" else host_l[10])
                    all_dic[b_name][env_name]["bigdata"][7] += 1

            else:
                # 在IpConfig 表内没有的服务器
                print("db tables is not ip:%s" % host_l[0])


def all_dic_rate():
    for k,v in all_dic.items():
        for kk,vv in v.items():
            if vv["service"][0] != 0:
                use_rate = vv["service"][1]/vv["service"][0]*100
                vv["service"][2] = use_rate
                use_rate = vv["service"][4]/vv["service"][3]*100
                vv["service"][5] = use_rate
                cpu_rate = float('%0.2f' % (vv["service"][6] / vv["service"][7]))
                vv["service"][6] = cpu_rate
                # print(cpu_rate,vv["service"][6],vv["service"][7],vv)

            if vv["bigdata"][0] != 0:
                use_rate = vv["bigdata"][1]/vv["bigdata"][0]*100
                vv["bigdata"][2] = use_rate
                use_rate = vv["bigdata"][4]/vv["bigdata"][3]*100
                vv["bigdata"][5] = use_rate
                cpu_rate = float('%0.2f'%(vv["bigdata"][6]/vv["bigdata"][7]))
                vv["bigdata"][6] = cpu_rate
                # print(cpu_rate,vv["bigdata"][6],vv["bigdata"][7],vv)

def insert_all():
    time_obj = models.RecordingTime.objects.filter().last()
    now_n = datetime.datetime.now()
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    if time_obj:
        if str(time_obj.pub_date) == now:
            time_id = time_obj.id
            print("时间存在")
        else:
            print("新建")
            time_id = models.RecordingTime.objects.create(pub_date=now_n).id

    else:
        time_id = models.RecordingTime.objects.create(pub_date=now_n).id

    for k,v in all_dic.items():
        for kk,vv in v.items():
            e_obj = models.Environment.objects.get(name=kk,to_b__name=k)
            if vv["service"][0] != 0:
                models.AllData.objects.update_or_create(env_id=e_obj.id, time_id=time_id, type=0,defaults={
                    "type":0,"memorytotal":vv["service"][0],"memoryuse":vv["service"][1],"memoryrate":float("%0.2f"%vv["service"][2]),
                    "disktotal":vv["service"][3],"diskuse":vv["service"][4],"diskrate":float("%0.2f"%vv["service"][5]),
                    'cpurate': vv["service"][6]
                })

            if vv["bigdata"][0] != 0:
                models.AllData.objects.update_or_create(env_id=e_obj.id, time_id=time_id, type=1,defaults={
                    "type":1,"memorytotal":vv["bigdata"][0],"memoryuse":vv["bigdata"][1],"memoryrate":float("%0.2f"%vv["bigdata"][2]),
                    "disktotal":vv["bigdata"][3],"diskuse":vv["bigdata"][4],"diskrate":float("%0.2f"%vv["bigdata"][5]),
                    'cpurate': vv["bigdata"][6]
                })








if __name__ == '__main__':
    # 创建基础数据表
    create_dic()
    # 存所有salt列表
    salt_all_data = []
    # 存返回数据
    salt_list = []
    # salt api run
    for salt_info in settings.salt_api_config:
        salt_obj = SaltApi(salt_info['ip_port'], salt_info["user"], salt_info["passwd"])
        salt_result = salt_obj.cmd(
            {"client": "local", "fun": "cmd.script", "arg": ['salt://scripts/zy.sh', 'aaa'], "tgt": "*"})
        salt_list.extend(salt_obj.all_list())
        salt_all_data.extend(salt_result)


    # 插入IpInfo 表数据
    insert_db(salt_all_data)

    # 不插入只计算
    # insert_db(salt_all_data,status=False)

    # 计算各个项目的总量
    all_dic_rate()
    # print(all_dic)

    # 插入AllData 表的数据
    insert_all()

    print("失败列表: ",set(salt_list) - set(ok_list))