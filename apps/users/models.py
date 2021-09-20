from django.db import models
from django.http import HttpResponseRedirect
from .forms import RegistrationForm


# Create your models here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'users/register.html', {'form': form})
