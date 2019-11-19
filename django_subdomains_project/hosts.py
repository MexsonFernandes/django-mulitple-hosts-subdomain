from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www', 'www.urls', name='www'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'app2', 'app2.urls', name='app2'),
)