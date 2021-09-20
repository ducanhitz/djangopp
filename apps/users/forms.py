from django import forms
from django.contrib.auth.models import User
import re


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password(self):
        if self.password1 == self.password2 and self.password1:
            return self.password2
        raise forms.ValidationError('Mat khau khong khop!')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username chua ky tu dac biet!')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username da ton tai!')

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
