# coding: utf-8
# db_outage/constants.py

"""Constants definitions for db_outage."""


import datetime

from django.conf import settings


__author__ = 'David Voegtle (dvoegtle@austin.utexas.edu)'


VIPRT_OUTAGE = (datetime.datetime(2016, 7, 9, 8), datetime.datetime(2016, 7, 9, 18),)
VIPR_OUTAGE = (datetime.datetime(2016, 7, 9, 8), datetime.datetime(2016, 7, 10, 18),)


def is_vipr_outage():
    """Determine by environment if outage is known."""
    today = datetime.datetime.now()
    if settings.PYPE_SERVICE in ('BETA', 'PROD',):
        return today >= VIPR_OUTAGE[0] and today <= VIPR_OUTAGE[1]
    return today >= VIPRT_OUTAGE[0] and today <= VIPRT_OUTAGE[1]

IS_SCHEDULED_OUTAGE = is_vipr_outage()
