# coding: utf-8
# db_outage/views.py

"""Default view to display outage message when the database is inaccessible."""


from __future__ import unicode_literals

from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from django.conf import settings


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


class ServiceUnavailableTemplateResponse(TemplateResponse):
    """Render a template response with status code 503 (service unavailable)."""

    status_code = 503


class DBOutage(TemplateView):
    """Render template to display outage message to users."""

    template_name = 'db_outage/db_outage.html'
    response_class = ServiceUnavailableTemplateResponse

    def get_context_data(self, **kwargs):
        """Add some data to the regular context."""
        context = super(DBOutage, self).get_context_data(**kwargs)
        context.update({
            'contact': getattr(settings, 'SECU_FAILED_CONTACT_EMAIL', 'viphelp@austin.utexas.edu'),
        })

        return context
