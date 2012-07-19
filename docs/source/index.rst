.. django-users documentation master file, created by
   sphinx-quickstart on Thu Jul 19 12:19:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-users's documentation!
========================================

Contents:

.. toctree::
   :maxdepth: 2

Installation
============

pip install django-users

Add 'django-users' to INSTALLED_APPS

Add (r'^users/', include('django_users.urls'))

url(r'^users/', include('django_users.backends.confirmationemail.urls')),

to urls.py

Usage
=====



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

