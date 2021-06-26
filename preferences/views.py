from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from .forms import PreferenceModelForm
from .models import Preference
# Create your views here.

class MyPreferenceFormView(FormView):
    form_class = PreferenceModelForm
    template_name = 'preferences/main.html'

    def get_success_url(self):
        #this will redirect to same page afte submision of form
        return self.request.path 

    def form_valid(self,form):
        form.save()
        messages.add_message(self.request,messages.INFO,'Data Saved Successfully')
        return super().form_valid(form)

    def form_invalid(self,form):
        form.add_error(None,'OOps something went wrong')
        return super().form_invalid(form)