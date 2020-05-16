from django.conf.urls import url
from django.urls import path , include
from . import views

app_name = 'posts'

urlpatterns = [
    path('' , views.listPost , name='listPost'),
    path('<slug:slug>', views.postsDetails,name='detailPost')
]
