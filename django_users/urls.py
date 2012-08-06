# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, password_change, password_change_done,\
        password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from longerusername.forms import AuthenticationForm

urlpatterns = patterns('',
                       url(r'^login/$',
                           login,
                           {
                               'template_name': 'users/login.html',
                               'authentication_form': AuthenticationForm,
                               },
                           name='auth_login'),
                       url(r'^logout/$',
                           logout,
                           {'template_name': 'users/logout.html'},
                           name='auth_logout'),
                       url(r'^password/change/$',
                           password_change,
                           name='auth_password_change'),
                       url(r'^password/change/done/$',
                           password_change_done,
                           name='auth_password_change_done'),
                       url(r'^password/reset/$',
                           password_reset,
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^password/reset/done/$',
                           password_reset_done,
                           name='auth_password_reset_done'),
)

