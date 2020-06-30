from django.conf.urls import url

from apps.user.views.home import index
from apps.user.views.account import login, register, send_sms, login_sms

urlpatterns = [
    url(r'^login/$', login, name='login'),  # 密码登录
    url(r'^loginsms/$', login_sms, name='login_sms'),  # 短信登录
    url(r'^register/', register, name='register'),
    url(r'^send_sms/', send_sms, name='send_sms'),

    url(r'^$', index, name='index'),


]
