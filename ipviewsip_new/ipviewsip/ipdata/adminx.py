import xadmin
from xadmin import views

from . import models

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "服务器信息管理系统"  # 设置站点标题
    site_footer = "理工新源运维部"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)


class BussinessUnitAdmin(object):

    list_display = ['name']

xadmin.site.register(models.BusinessUnit,BussinessUnitAdmin)

class EnvironmentAdmin(object):

    list_display = ['name','to_b']

xadmin.site.register(models.Environment,EnvironmentAdmin)

class IpConfigAdmin(object):
    search_fields = ["ip"]

    list_display = ['ip','type','env']

xadmin.site.register(models.IpConfig,IpConfigAdmin)

