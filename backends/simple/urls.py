#coding=utf-8
from django.conf.urls.defaults import *
from  perfiles.urls import urlpatterns as baseurlpatterns
from perfiles.backends.simple.views import CreateUser

urlpatterns = patterns('',
        url(r'^register/$',
            CreateUser.as_view(),
            name='register'
            ),
)

urlpatterns += patterns('',
        url(r'^', include(baseurlpatterns)),
)
