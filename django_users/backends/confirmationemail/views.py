# -*- coding: utf-8 -*-
"""
This backend creates a deactivated user, and sends an email with the confirmation code.
"""
from django_users.views import CreateUserBase
from django.template import Context, loader
#from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext as _
from django.core import signing
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
#from templated_email import send_templated_mail
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
import logging

logger = logging.getLogger(__name__)

class CreateUser(CreateUserBase):
    signer = signing.TimestampSigner(salt='registerkey')

    def _send_activation_email(self, user):
        signed_key = self.signer.sign(user.username)

        site = Site.objects.get_current()
        url = reverse('activate', args=[signed_key,])
        full_url = 'http://%s%s' % (site.domain, url)
        t = loader.get_template('mails/activation.txt')
        data = {
                'url': full_url,
                'site': site,
        }
        content = t.render(Context(data))
        send_mail(_(u'Activate your account in %(site_name)s' % {'site_name':site.name,}), content, settings.DEFAULT_FROM_EMAIL,
                    [user.email,], fail_silently=False)
        #context ={
                #}
        #send_templated_mail(
                #template_name='default',
                ##from_email='from@example.com',
                #recipient_list=[user.email,],
                #context=context,
        #)
        #signed_key = self.signer.sign(user.username)
        #print signed_key

    def response_after_success(self):
        """
        Response returned after the object has been saved.
        """
        url = reverse('activation-sent')
        return HttpResponseRedirect(url)

    def get_username(self, data):
        return data['username']

    def get_email(self, data):
        return data['email']

    def get_password(self, data):
        return data['password']

    def save_user(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(self.get_username(data), self.get_email(data), self.get_password(data))
        user.is_active = False
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.save()
        # Send the activation email
        self._send_activation_email(user)
        return user

    #SignatureExpired
    #try:
    #...    original = signer.unsign(value)
    #... except signing.BadSignature:
    #...    print "Tampering detected!"

class Activate(TemplateView):
    signer = signing.TimestampSigner(salt='registerkey')
    template_name = 'users/confirmationemail/activate.html'

    def dispatch(self, request, *args, **kwargs):
        key = args[0]
        try:
            username = self.signer.unsign(key, max_age=3600*24*7)
        except signing.BadSignature:
            logger.critical('Bad signature with the key: %s' % (key, ))
            raise Http404
        except signing.SignatureExpired:
            logger.info('Signature expired for the user %s' % (username, ))
            raise Http404

        user = get_object_or_404(User, username=username)
        user.is_active=True
        user.save()

        # Login the user
        #login(request, user)

        return super(Activate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Activate, self).get_context_data(**kwargs)
        redirect = getattr(settings, 'ACTIVATION_REDIRECT', settings.LOGIN_REDIRECT_URL)
        context['ACTIVATION_REDIRECT'] = redirect
        return context

