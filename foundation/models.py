from django.db import models

class MainPage(models.Model):
    name              = models.CharField(max_length = 200)
    url               = models.URLField(max_length = 2000)
    title             = models.CharField(max_length = 200)
    description       = models.CharField(max_length = 400)
    hover_description = models.CharField(max_length = 400)
    size              = models.IntegerField()

    class Meta:
        db_table = 'main_pages'

class Instagram(models.Model):
    thumbnail     = models.URLField(max_length = 2000)
    profile_image = models.URLField(max_length = 2000)
    user          = models.CharField(max_length = 100)
    created       = models.CharField(max_length = 100)

    class Meta:
        db_table = 'instagrams'

class Store(models.Model):
    name       = models.CharField(max_length = 50)
    address1   = models.CharField(max_length = 300)
    address2   = models.CharField(max_length = 300)
    city       = models.CharField(max_length = 45)
    phone      = models.CharField(max_length = 100)
    longitude  = models.CharField(max_length = 100)
    latitude   = models.CharField(max_length = 100)
    state      = models.CharField(max_length = 30)
    store_type = models.CharField(max_length = 30)

    class Meta:
        db_table = 'stores'
