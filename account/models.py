from django.db import models

class User(models.Model):
    email         = models.EmailField(max_length=300)
    password      = models.CharField(max_length=400)
    name          = models.CharField(max_length=400)
    phone         = models.CharField(max_length=20)
    birth         = models.CharField(max_length=20)
    gender        = models.BooleanField()
    email_confirm = models.BooleanField()
    text_confirm  = models.BooleanField()
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
