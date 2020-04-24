from django.db import models

class User(models.Model):
    email         = models.EmailField(max_length = 300)
    password      = models.CharField(max_length = 400)
    name          = models.CharField(max_length = 400)
    phone         = models.CharField(max_length = 20)
    birth         = models.CharField(max_length = 20)
    email_confirm = models.BooleanField()
    text_confirm  = models.BooleanField()
    gender        = models.ForeignKey('Gender', on_delete = models.SET_NULL, null = True)
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'

class Gender(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'genders'
