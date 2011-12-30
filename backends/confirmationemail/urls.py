#coding=utf-8
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from  perfiles.urls import urlpatterns as baseurlpatterns
from perfiles.backends.confirmationemail.views import Activate, CreateUser

urlpatterns = patterns('',
        url(r'^register/$',
            CreateUser.as_view(),
            name='register'
            ),
        url(r'^activation-sent/$',
            direct_to_template,
            {'template':'registration/confirmationemail/activation-sent.html',},
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
