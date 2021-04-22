from django.db import models

import datetime

class User(models.Model):
    name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Электронная почта')
    birthday = models.DateField('Дата рождения')
    registration_date = models.DateField('Дата регистрации', default=datetime.date.today)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'main_user'

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)

