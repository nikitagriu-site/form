from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import User
from django.contrib import messages
from .forms import AddUser


def home(request):
    form = AddUser(request.POST)
    if request.method == 'POST' and form.is_valid():
        if form.is_valid():
            print(form.cleaned_data)
            try:
                User.objects.create(**form.cleaned_data)
                return redirect('home.html')
            except:
                form.add_error("Ошибка регистрации")
    return render(request, 'home.html', {'form' : form})

