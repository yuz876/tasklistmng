from django.urls import path

from . import views

appname = "tasklistmng"

urlpatterns = [
    path('', views.index, name='index'),
    path('signin.html', views.signin, name='signin'),
    path('signon.html', views.signon, name='signon'),
]