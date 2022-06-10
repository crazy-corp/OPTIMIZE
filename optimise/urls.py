"""optimise URL Configuration

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
from django.urls import path
from gallery import views as g_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",g_v.index,name="index"),
    path("submit",g_v.submit,name="submit"),
    path("2",g_v.index2,name="index2"),
    path("submit2",g_v.submit2,name="submit2"),
    path("3",g_v.index3,name="index3"),
    path("submit3",g_v.submit3,name="submit3"),

]
