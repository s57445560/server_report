from django.contrib import admin

# Register your models here.

#导⼊模型
from ipdata.models import BusinessUnit,Environment,IpConfig
# Register your models here.

class ArticleAdmin1(admin.ModelAdmin):
    list_display = ('name',) # 设置多字段显示
    list_filter = ('name',) # 显示过滤字段
    list_per_page = 50 # 每页显示 50 条记录

class ArticleAdmin2(admin.ModelAdmin):
    list_display = ('name',) # 设置多字段显示
    list_filter = ('name',) # 显示过滤字段
    list_per_page = 50 # 每页显示 50 条记录

class ArticleAdmin3(admin.ModelAdmin):
    list_display = ('ip',"type",) # 设置多字段显示
    list_filter = ('type',) # 显示过滤字段
    list_per_page = 50 # 每页显示 50 条记录
#注册事业部模型
admin.site.register(BusinessUnit,ArticleAdmin1)
#注册环境模型
admin.site.register(Environment,ArticleAdmin2)
#注册配置模型
admin.site.register(IpConfig,ArticleAdmin3)


admin.site.site_header = '信息后台管理'
admin.site.site_title = '信息后台管理页面'
admin.site.index_title = '欢迎使用后台管理页面'

