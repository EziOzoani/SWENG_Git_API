from django.conf.urls import url
from yokogao import views 

urlpatterns = [
    url(r'^$', views.index , name='index'),
]