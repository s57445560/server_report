#!/bin/bash

# ip
ip=`ifconfig|grep -Po '[\d]+\.[\d]+\.[\d]+\.[\d.]+'|egrep '^(10\.|192\.)'|egrep -v "^10.244"|head -1`





# --------------------------- 内存
# 内存总量
mem=`free -m|awk 'NR==2{print $2}'`


if `cat /etc/redhat-release |grep " 6\.">/dev/null`;then
    mem=`free -m|awk 'NR==2{print $2}'`
    mem_b=`free -m|awk 'NR==2{printf "%.2f%",100-($4+$6+$7)/$2*100}'`
    mem_use=`free -m|awk 'NR==2{print $2-($4+$6+$7)}'`
else
    mem=`free -m|awk 'NR==2{print $2}'`
    mem_b=`free -m|awk 'NR==2{printf "%.2f%",(100-($4+$6)/$2*100)}'`
    mem_use=`free -m|awk 'NR==2{print $2-($4+$6)}'`
fi



# --------------------------- cpu
# cpu核心数
cpu_number=`cat /proc/cpuinfo |grep processor|wc -l`

# cpu load第一个数

cpu_load=`sar -q 2>/dev/null|egrep '^[0-9]'|awk 'NR>1{a+=$5}END{printf "%.3f",a/NR}'`


# cpu use
cpu_b=`sar -u 2>/dev/null|egrep '^[0-9]'|awk -F' ' 'NR>1{a+=$3}END{printf "%.2f",a/NR}'`

# --------------------------- 磁盘
# 磁盘容量总是
disk_all_number=`fdisk -l 2>/dev/null|grep "/dev/sd[a-z]:"|awk '{a+=$3}END{print a}'`
disk_use=`df -Pm|egrep -v "(docker|kubelet)"|grep -Pv '^[0-9]'|awk 'NR!=1{a+=+$3}END{printf "%.1f\n",a/1024}'`

disk_b=`awk 'BEGIN{printf "%.2f%",'$disk_use'/'$disk_all_number'*100}'`


# --------------------------- 机器类型判断
# 判断机器类型
type=`dmidecode -s system-product-name|grep VMware >/dev/null&&echo '虚拟机'||echo '物理机'`



# IP地址|总能存|内存使用率|cpu核心数|cpuload值|磁盘总容量|磁盘使用容量|磁盘使用率|服务类型|cpu使用率
echo "$ip|$mem|$mem_use|$mem_b|$cpu_number|$cpu_load|$disk_all_number|$disk_use|$disk_b|$type|$cpu_b"



