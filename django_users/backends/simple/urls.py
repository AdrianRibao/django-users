#coding=utf-8
from django.conf.urls.defaults import *
from  django_users.urls import urlpatterns as baseurlpatterns
from django_users.backends.simple.views import CreateUser

urlpatterns = patterns('',
        url(r'^register/$',
            CreateUser.as_view(),
            name='register'
            ),
)

urlpatterns += patterns('',
        url(r'^', include(baseurlpatterns)),
)
