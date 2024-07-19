from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import Usercreation


class Signupnew(generic.CreateView):
    form_class = Usercreation
    template_name = 'registration/sigup.html'
    success_url = reverse_lazy('login')
