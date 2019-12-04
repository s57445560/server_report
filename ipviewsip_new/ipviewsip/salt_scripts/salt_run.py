#!/usr/bin/python
# coding=utf8
# author: Sun yang

import salt.client
import pickle
local = salt.client.LocalClient()
result = local.cmd_iter('*','cmd.script',['salt://scripts/zy.sh'],expect_minions=True)

pickle_list = [[]]
for host in result:
    host_result_status = host.values()[0].get("failed",False)
    if  host_result_status:
        pickle_list[0].append(host)
        continue
    pickle_list.append(host)

with open('10.10.7.6.pkl','wb') as f:
    pickle.dump(pickle_list,f)

