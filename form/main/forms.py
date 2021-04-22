from django import forms

from .models import User

import datetime

class AddUser(forms.Form):
    name = forms.CharField(label="Имя", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    phone_number = forms.CharField(label="Номер телефона", max_length=20)
    email = forms.EmailField(label="Электронная почта")
    birthday = forms.DateField(label="Дата рождения")

