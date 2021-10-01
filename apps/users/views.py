from django import forms
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, FormView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

# Create your views here.


class SiteLoginView(LoginView):
    template_name = 'login.html'

class SiteLogoutView(LogoutView):
    template_name = 'logout.html'


class SiteRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'data-id': 1000}))

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}


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
        url = f"{reverse('register_ok')}?username={new_user.username}"
        return redirect(url)

class SiteRegisterViewOk(TemplateView):
    template_name = 'register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
