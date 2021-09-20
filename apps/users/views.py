from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm

# Create your views here.
def Index(request):
    return HttpResponse('hello')

def Register(request):
    form = RegistrationForm()
    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('helloworld/')
    return render(request, 'users/register.html', {'form': form})

