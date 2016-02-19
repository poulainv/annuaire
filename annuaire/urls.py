from annuaire import settings

from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'admin', include(admin.site.urls)),
    url(r'', include('app.urls'))
]

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
