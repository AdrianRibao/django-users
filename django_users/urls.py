# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import logout, password_change, password_change_done,\
        password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.forms import AuthenticationForm
from django_users.settings import LOGIN_VIEW

urlpatterns = patterns('',
                       url(r'^login/$',
                           LOGIN_VIEW,
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
                           {'template_name': 'users/password-reset.html'},
                           name='auth_password_reset'),
                       url(r'^password/reset/done/$',
                           password_reset_done,
                           {'template_name': 'users/password-reset-done.html'},
                           name='auth_password_reset_done'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           password_reset_confirm,
                           {'template_name': 'users/password-reset-confirm.html'},
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           password_reset_complete,
                           {'template_name': 'users/password-reset-complete.html'},
                           name='auth_password_reset_complete'),
)

