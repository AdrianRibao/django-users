#coding=utf-8
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django_users.urls import urlpatterns as baseurlpatterns
from django_users.backends.confirmationemail.views import Activate, CreateUser
from django_users.forms import CreateUserForm

urlpatterns = patterns('',
        url(r'^register/$',
            CreateUser.as_view(form_class=CreateUserForm),
            name='register'
            ),
        url(r'^activation-sent/$',
            direct_to_template,
            {'template':'users/confirmationemail/activation-sent.html',},
            name='activation-sent'
            ),
        url(r'^activate/(.+)/$',
            Activate.as_view(),
            name='activate'
            ),
)

urlpatterns += patterns('',
        url(r'^', include(baseurlpatterns)),
)
