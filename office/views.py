from django.utils.translation import ugettext as _
from django.views.generic import ListView 
from .forms import OfficeForm , AddressForm
from .models import Address ,Office 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalCreateView)

class OfficeListView(ListView):
	model = Office
	template_name = 'office/list_office.html'
	success_url = reverse_lazy('office:office-list')    


class OfficeCreateView(BSModalCreateView):
	form_class = OfficeForm
	second_form_class = AddressForm
	template_name = 'office/create_office.html'
	success_url = reverse_lazy('office:office_list')    

	def get_context_data(self, **kwargs):
		context = super(OfficeCreateView, self).get_context_data(**kwargs)
		context['form1'] = self.second_form_class
		return context

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)
		form = self.form_class
		form1 = self.second_form_class
		
		return self.render_to_response(self.get_context_data(
			object=self.object, form=form, form1=form1))

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		form1 = self.second_form_class(request.POST)
		if not self.request.is_ajax():
			if form1.is_valid() and form.is_valid():
				address = form1.save()
				office = form.save(commit=False)
				office.address = address
				office.save()
				return redirect('office:office_list')
			else:
				return super(OfficeCreateView, self).post(request, *args, **kwargs)
		else:
			return super(OfficeCreateView, self).post(request, *args, **kwargs)
    