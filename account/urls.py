#coding:utf-8
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 登陆 / 登出 urls
    url(r'^login/$',
        'django.contrib.auth.views.login',name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^logout-then-login/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    # 更改密码 urls
    url(r'^password-change/$',
       'django.contrib.auth.views.password_change',
       name='password_change'),
    url(r'^password-change/done/$',
       'django.contrib.auth.views.password_change_done',
       name='password_change_done'),
    # 重置密码 urls
    url(r'^password-reset/$',
        'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(r'^password-reset/done/$',
         'django.contrib.auth.views.password_reset_done',
         name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
           'django.contrib.auth.views.password_reset_confirm',
         name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
         'django.contrib.auth.views.password_reset_complete',
          name='password_reset_complete'),
    # 注册登陆
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    # 社交账户登陆 urls
    url('social-auth/',include('social.apps.django_app.urls', namespace='social')),
]

