# -*- coding: utf-8 -*-
"""
This backend just create the user
"""

from django_users.views import CreateUserBase
from django.contrib.auth.models import User

class CreateUser(CreateUserBase):
    def save_user(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(data['username'], data['email'], data['password'])
        user.is_active = True
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        return user
