#!/bin/bash

# pull of salt_run.py result  pickle file
echo "now time ---> `date`"

>10.11.8.1.pkl
>10.10.7.6.pkl
report_path=/opt/mid_app/report

# 10.11.8.1 run salt
ssh 10.11.8.1 ">/opt/mid_app/report/10.11.8.1.pkl"
ssh 10.11.8.1 "cd /opt/mid_app/report;python2.6 salt_run.py"

scp 10.11.8.1:/opt/mid_app/report/10.11.8.1.pkl ./
echo "10.11.8.1 run salt ok!"


# 10.10.7.6 run salt
ssh 10.10.7.6 ">/opt/mid_app/report/10.10.7.6.pkl"
ssh 10.10.7.6 "cd /opt/mid_app/report;python2.7 salt_run.py"

scp 10.10.7.6:/opt/mid_app/report/10.10.7.6.pkl ./

echo "10.10.7.6 run salt ok!"

python3 create_salt.py
