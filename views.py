# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.contrib.auth.models import User
from perfiles.forms import CreateUserForm
from django.utils.importlib import import_module
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.http import HttpResponseRedirect

class CreateUserBase(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = CreateUserForm
    success_url = '/'

    def save_user(self, form):
        raise NotImplementedError("The class must provide a save_user method")

    def response_after_success(self):
        """
        Response returned after the object has been saved.
        """
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        user = self.save_user(form)
        self.object = user
        return self.response_after_success()

class Register(View):

    # Function inspired in django registration: django-registratin /registration/backends/__init__.py

    def _get_backend(self):
        """
        Return an instance of a registration backend.

        If the backend cannot be located (e.g., because no such module
        exists, or because the module does not contain a class of the
        appropriate name), ``django.core.exceptions.ImproperlyConfigured``
        is raised.
        """

        module = getattr(settings, 'PERFILES_BACKEND', 'perfiles.backends.simple')
        module_views = '%s.views' % (module, )

        try:
            mod = import_module(module_views)
        except ImportError, e:
            raise ImproperlyConfigured('Error loading registration backend %s: "%s"' % (module, e))

        try:
            backend_class = getattr(mod, 'CreateUser')
        except AttributeError:
            raise ImproperlyConfigured('Module "%s" does not define a registration backend named "CreateUser"' % (module, ))
        return backend_class()

    def dispatch(self, request, *args, **kwargs):
        backend = self._get_backend()
        return backend.dispatch(request, *args, **kwargs)


