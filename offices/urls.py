from django.conf.urls import patterns, include, url
from .views import OfficeDetailsView

urlpatterns = patterns('', 
	url(r'officedetails/(?P<id>\d+)/$', OfficeDetailsView.as_view(), name="Office Details"),
)