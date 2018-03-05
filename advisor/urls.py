from django.conf.urls import patterns, url
from django.contrib import admin

import advisor.views

admin.autodiscover()

urlpatterns = patterns('',
    # viewer management
    url(r'^addAdvisor/$', advisor.views.AdvisorView.as_view()),
    url(r'^addAdvisor/(?P<sem_name>.+?)/(?P<sem_year>[0-9]{4})/(?P<email>.+?)/$',
        advisor.views.AdvisorView.as_view()),
)