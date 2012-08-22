# -*- coding: utf-8 -*-
from django import template
from django_users.forms import CreateUserForm
#from django.utils.translation import ugettext as _

register = template.Library()

@register.inclusion_tag('users/templatetags/registration.html', takes_context = True)
def registration_form(context, form=None, *args, **kwargs):
    if not form:
        form = CreateUserForm
    return {
            'form': form,
    }


