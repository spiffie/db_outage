# coding: utf-8
# db_outage/urls.py

"""Urls definitions for db_outage app."""


from django.conf.urls import url

from .views import DBOutage


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


urlpatterns = [
    # Hook this in to your URL structure somehwere if you want to view a rendered template.
    url(r'^$', DBOutage.as_view(), name='db_outage_test'),
]
