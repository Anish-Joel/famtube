from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (CreateView)
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.

class Userview(PasswordChangeView):
    template_name ='pass.html'
    form_class =PasswordChangeView
    
    success_url = reverse_lazy('family')
class Userview(CreateView):
    template_name ='sa.html'
    form_class =UserCreationForm
    queryset =User.objects.all()
    success_url ='../family/login/'
  