"""zny_conference_manage URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', views.logout),
    url(r'^login/', views.login),
    url(r'^conference/(?P<conference_id>\d+)', views.conference_detail),
    url(r'^conference/$', views.conference),
    url(r'^add_confer/$', views.add_conference),
    url(r'^edit_conference/(?P<conference_id>\d+)/', views.edit_conference),
    url(r'^del_conference/(?P<conference_id>\d+)/', views.del_conference),
]
