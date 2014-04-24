from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from dashboard.views import JobListView

urlpatterns = patterns('',
    url(r'^$', JobListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
