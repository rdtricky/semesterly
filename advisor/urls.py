from django.conf.urls import patterns, url
from django.contrib import admin

import advisor.views

admin.autodiscover()

urlpatterns = patterns('',
    # viewer management
        url(r'^addAdvisor/$', advisor.views.AdvisorView.as_view()),
#     url(r'^add_advisor/*$', FeatureFlowView.as_view(feature_name='ADD_ADVISOR')),
)
