"""Default view to display outage message when the database is inaccessible."""

# db_outage/views.py
# coding: utf-8


from __future__ import unicode_literals

import datetime

# from django.core.exceptions import ImproperlyConfigured
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView
from django.conf import settings


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


# TODO: When this is scheduled, update this to the correct begin and end dates.
VIPRT_OUTAGE = (datetime.date(2050, 1, 1), datetime.date(2050, 1, 1),)
VIPR_OUTAGE = (datetime.date(2050, 1, 1), datetime.date(2050, 1, 1),)


class ServiceUnavailableTemplateResponse(TemplateResponse):
    """Render a template response with status code 503 (service unavailable)."""

    status_code = 503


class DBOutage(TemplateView):
    """Render template to display outage message to users."""

    template_name = 'db_outage/db_outage.html'
    response_class = ServiceUnavailableTemplateResponse

    def _is_vipr_outage(self):
        today = datetime.date.today()
        if settings.PYPE_SERVICE in ('BETA', 'PROD',):
            return today >= VIPR_OUTAGE[0] and today <= VIPR_OUTAGE[1]
        return today >= VIPRT_OUTAGE[0] and today <= VIPRT_OUTAGE[1]

    def get_context_data(self, **kwargs):
        """Add some data to the regular context."""
        context = super(DBOutage, self).get_context_data(**kwargs)
        context.update({
            'contact': getattr(settings, 'SECU_FAILED_CONTACT_EMAIL', 'viphelp@austin.utexas.edu'),
            'vipr_outage': self._is_vipr_outage(),
        })

        return context

        # TODO: Plausibly for a standard outage page we don't need it to be that configurable.
        # ctx = super(DBOutage, self).get_context_data(**kwargs)
        # try:
        #     msg = settings.DB_OUTAGE_MESSAGE
        # except AttributeError:
        #     raise ImproperlyConfigured(
        #         'You must add a DB_OUTAGE_MESSAGE to your settings. Example: '
        #         'We are experiencing technical difficulties. Our IT staff has '
        #         'been notified.'
        #     )
        # ctx.update({'msg': msg})
        # return context(
        #     self.request,
        #     ctx,
        #     title='Service Outage',
        #     page_title='Service Outage',
        #     window_title='Service Outage',
        # )
