from django.urls import path

from . import views

appname = "tasklistmng"

urlpatterns = [
    path('', views.index, name='index'),
]