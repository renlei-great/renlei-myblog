from django.conf.urls import url

from user.views.home import index
from user.views.account import login, register, send_sms

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^send_sms/', send_sms, name='send_sms'),


    url(r'^$', index, name='index'),


]
