from django.conf.urls import url

from . import views
from helpers.mixins import FeatureFlowView

urlpatterns = [
    # url('', views.index, name='^add_advisor/*$'),
    url(r'^add_advisor/*$', FeatureFlowView.as_view(feature_name='ADD_ADVISOR')),
]