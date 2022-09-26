"""jobsinformation URL Configuration

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
"""
from django.urls import include, re_path
from django.contrib import admin
from jobsapp import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index),
    re_path(r'^punejobs/', views.punejobs),
    re_path(r'^hydjobs/', views.hydjobs),
    re_path(r'^chennaijobs/', views.chennaijobs),
    re_path(r'^banglorejobs/', views.banglorejobs),
    re_path(r'^register/', views.student_view),
    re_path(r'^thankyou/', views.thankyou_view),
    re_path(r'^studentlist/', views.list_student),
    re_path(r'^signup/', views.signup_view),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^api/', include('jobsapp.api.urls')),
]
