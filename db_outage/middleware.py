"""Default view to display outage message when the database is inaccessible."""

# db_outage/views.py
# coding: utf-8


from __future__ import unicode_literals

import logging
import sys

from django.conf import settings
# from django.core.mail import mail_admins
from django.db import connections
from django.db.utils import DatabaseError as django_DatabaseError

import cx_Oracle

from db_outage.views import DBOutage


logger = logging.getLogger('django')

_using_manage = True in ['manage.py' in arg for arg in sys.argv]

TESTING = ((_using_manage and 'test' in sys.argv) or ('nosetests' in sys.argv))


class DBOutageMiddleware(object):
    """Wrap requests with function that tests for database availability."""

    def process_request(self, request):
        """Ping database, and if down log message and return standard outage view.

        # Django tests may set their own ROOT_URLCONF, in which case we may not
        # be able to resolve 'db_outage', so we'll just return None unless
        # testing this app intentionally.
        """
        # TODO: Possibly we don't need this?
        # if TESTING and {'db_outage', 'test_db_outage'}.isdisjoint(sys.argv):
        #     return None

        if settings.STATIC_URL in request.path:
            return None

        try:
            self._ping_db()
        except (django_DatabaseError, cx_Oracle.DatabaseError) as exc:
            # msg = (
            #     'Your application is having trouble connecting to the '
            #     'database. Please investigate.'
            # )
            # mail_admins('DatabaseError', msg)
            logger.error(exc)
            return DBOutage.as_view()(request)

        return None

    def _ping_db(self, db='default'):
        with connections[db].cursor() as cursor:
            cursor.execute("SELECT 1 FROM DUAL")
        return None
