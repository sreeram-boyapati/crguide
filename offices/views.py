# Create your views here.
# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.views.generic import ListView, View, UpdateView
from django.shortcuts import render
from .models import Office
from django.http.response import HttpResponse, HttpResponseRedirect
from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin


class OfficeDetailsView(DetailView):
	template_name = 'office_details.html'
	model = Office

	def get_object(self):
		return Office.objects.get(id=self.kwargs['id'])