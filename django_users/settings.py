# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.views import login

# The login view to be used. Userful if you want to apply a decorator
LOGIN_VIEW = getattr(settings, 'LOGIN_VIEW', login)
