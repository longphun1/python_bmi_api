from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^accounts/profile/$', views.index),
    url(r'^processBmi', views.processBmi),
    url(r'^editBmi/(?P<data_id>\d+)', views.editBmi),
    url(r'^processEdit/(?P<data_id>\d+)', views.processEdit),
    url(r'^deleteBmi/(?P<data_id>\d+)', views.deleteBmi)
]