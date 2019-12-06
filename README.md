## 这事一个django写的 服务器报表服务


## 使用方法

```需要结合 salt使用，这里salt没有使用salt api, 直接远程登陆salt服务器，来执行任务，获取的基础数据。
脚本放在 salt_scripts目录下
xadmin来管理基础数据。
也可以结合自己的流程系统，来编写接口，自动触发，增加减少服务器。

需要登陆后台，设置事业部关联事业部使用的环境以及主机。剩下的基础属于使用定时任务来自动获取。


应用技术：
   Vue + rest framework

   ipweb 为Vue的源码。

   需要借助salt来获取基础数据，安装salt-api,使用create_salt.py 脚本来定时获取数据写入数据库。

   salt获取基础数据的shell脚本在salt_scripts/zy.sh，放在 salt服务器的 /srv/salt/scripts/zy.sh下
   zy.sh脚本需要使用sar命令和dmidecode 需要使用yum把依赖包安装上。


需要配置的如下:
   ipviewsip_new/ipviewsip/settings.py    修改salt-api连接的地址，端口，用户名，密码信息

   ipviewsip_new/ipviewsip/dist/static/project.config.json 修改前端访问后端的地址


```

## 页面展示

![image](https://github.com/s57445560/img-all/raw/master/server_report/home.png)
