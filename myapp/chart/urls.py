from django.conf.urls import url
from . import views
app_name = 'chart'
urlpatterns =[
url(r'^$', views.index, name='index'),
url(r'^chart-room/(?P<channel_id>[0-9]+)/$', views.room, name='room'),
url(r'^category/(?P<channel_id>[0-9]+)/$', views.category, name='category'),
url(r'^chat/Help$', views.Help, name='Help'),
url(r'^thought$', views.thought, name='thought'),
]
