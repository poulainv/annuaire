from annuaire import settings

from django.views.generic import TemplateView
from django.conf.urls import url, include, patterns

from . import views


urlpatterns = [
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^submission/', views.submit_project, name='submission'),
    url(r'^mentions-legales/', views.credits, name='mentions-legales'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^vote/', views.vote, name='vote'),
    url(r'^projects/(?P<pk>[0-9]+)$', views.ProjectDetailView.as_view(), name='project'),
    url(r'^projects/(?P<slug>[-\w]+)$', views.ProjectDetailView.as_view(), name='project'),
    url(r'^projects', views.ProjectIndexView.as_view(), name='projects'),
    url(r'', TemplateView.as_view(template_name="app/index.html"), name='home')
]


if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
    
