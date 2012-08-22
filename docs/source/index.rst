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

.. code::

    pip install django_users

Add ``'django_users'`` to ``INSTALLED_APPS``

Add the URLs to urls.py:

.. code::

    # Django users
    url(r'^users/', include('django_users.backends.confirmationemail.urls')),

Available views
===============

================= ====================
View              Name of the view
================= ====================
Login             auth_login
Logout            auth_logout
Password change   auth_password_change
Password reset    auth_password_reset
================= ====================

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

