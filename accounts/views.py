from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = RegisterForm()
        
    return render(request, "accounts/register.html", {"form": form})

def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                homeurl = reverse('home')
                return HttpResponseRedirect(homeurl)
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form':form})