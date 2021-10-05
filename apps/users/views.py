from django import forms
from django.urls import reverse
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, FormView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from apps.users.forms import SiteRegisterForm

# Create your views here.

User = get_user_model()


class SiteLoginView(LoginView):
    template_name = 'login.html'


class SiteLoginViewOk(TemplateView):
    template_name = 'profile.html'


class SiteLogoutView(LogoutView):
    template_name = 'logout.html'


class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = SiteRegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data['username'],
                                            password=data['password1'],
                                            email=data['email'])
        from pprint import pprint
        pprint(data)
        url = f"{reverse('register_success')}"
        return redirect(url)


class SiteRegisterViewSuccess(TemplateView):
    template_name = 'register_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'

    model = User
    fields = ('email', 'full_name', 'address', 'year_birth', 'about')
    success_url = reverse_lazy('profile')

    def get_object(self, request=None):
        return self.request.user
