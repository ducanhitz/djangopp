from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

# Create your views here.
class SiteLoginView(LoginView):
    template_name='login.html'

    
class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name='profile.html'