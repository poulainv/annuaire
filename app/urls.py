from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ProjectIndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='detail')
]
