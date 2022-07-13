"""day16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path('depart/list/',views.depart_list),
    re_path('depart/add/',views.depart_add),
    re_path('depart/delete/',views.depart_delete),
    re_path('depart/(\d+)/edit/',views.depart_edit),
    #用户管理
    re_path('user/list/',views.user_list),
    re_path('user/add/',views.user_add),
    re_path('user/model/form/add/',views.user_mdoel_form_add),
    re_path('user/(\d+)/delete/',views.user_delete),
    re_path('user/(\d+)/edit/',views.user_edit),

    #靓号列表
    re_path('mobile/list',views.mobile_list),
    re_path('mobile/add',views.mobile_add),
    re_path('mobile/(\d+)/edit',views.mobile_edit),
    re_path('mobile/(\d+)/delete',views.mobile_delete),

]
