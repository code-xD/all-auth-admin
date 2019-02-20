from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.


def home(request):
    if request.method == 'POST':
        if 'admin' in request.POST:
            print("admin signal fired.")
            settings.MOD_ADMIN = True
        elif 'user' in request.POST:
            print("user signal fired.")
            settings.MOD_ADMIN = False
        return redirect('/accounts/google/login')
    return render(request, 'adminapp/home.html')
