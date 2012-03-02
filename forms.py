# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label=_(u'Password'))
    password_confirm = forms.CharField(widget=forms.PasswordInput, label=_(u'Confirm the password'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password_confirm(self):
        if self.cleaned_data.get('password') and self.cleaned_data.get('password_confirm') and self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            raise forms.ValidationError(_(u"The passwords don't match"))
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            raise forms.ValidationError(_(u"The username has already been taken"))

        return self.cleaned_data
