#!/bin/bash

status=$1

if [[ $status == "start" ]];then
nohup python3 manage.py runserver 0.0.0.0:8000 &
else
ps -ef|grep "manage.py runserver"|grep -v grep|awk '{print $2}'|xargs kill -9
fi
