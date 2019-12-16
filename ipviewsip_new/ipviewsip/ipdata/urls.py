"""ipviewsip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

from django.conf.urls import include, url
from ipdata import views


urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/base_info$',views.Base_info.as_view(),name='base_info'),
    url(r'^(?P<version>[v1|v2]+)/ip_info$',views.Ip_info.as_view(),name='ip_info'),
    url(r'^(?P<version>[v1|v2]+)/all_info$',views.All_info.as_view(),name='all_info'),
    url(r'^(?P<version>[v1|v2]+)/download$',views.Download.as_view(),name='download'),
    url(r'^(?P<version>[v1|v2]+)/home$',views.Home.as_view(),name='home'),
    url(r'^(?P<version>[v1|v2]+)/memory$',views.Memory_table.as_view(),name='memory'),
    url(r'^(?P<version>[v1|v2]+)/disk$',views.Disk_table.as_view(),name='disk'),
    url(r'^(?P<version>[v1|v2]+)/cpu$',views.Cpu_table.as_view(),name='cpu'),
    url(r'^(?P<version>[v1|v2]+)/rate$',views.Rate_table.as_view(),name='rate'),
    url(r'^(?P<version>[v1|v2]+)/ipconfig$',views.Ipconfig.as_view(),name='ipconfig'),
    url(r'^(?P<version>[v1|v2]+)/resource_curve$',views.Resource_curve_table.as_view(),name='resource_curve'),

]

