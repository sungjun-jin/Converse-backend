from django.db import models

class MainPage(models.Model):
    name              = models.CharField(max_length = 200)
    url               = models.URLField(max_length = 2000)
    title             = models.CharField(max_length = 200)
    description       = models.CharField(max_length = 400)
    hover_description = models.CharField(max_length = 400)
    size              = models.IntegerField()
    code              = models.CharField(max_length = 30)

    class Meta:
        db_table = 'main_pages'

class Instagram(models.Model):
    thumbnail        = models.URLField(max_length = 2000)
    profile_image    = models.URLField(max_length = 2000)
    user             = models.CharField(max_length = 100)
    created_at       = models.CharField(max_length = 100)

    class Meta:
        db_table = 'instagrams'

class Store(models.Model):
    name       = models.CharField(max_length = 50)
    address1   = models.CharField(max_length = 300)
    address2   = models.CharField(max_length = 300)
    city       = models.CharField(max_length = 45)
    phone      = models.CharField(max_length = 20)
    longitude  = models.DecimalField(max_digits = 20, decimal_places = 15)
    latitude   = models.DecimalField(max_digits = 20, decimal_places = 15)
    state      = models.CharField(max_length = 30)
    store_type = models.ForeignKey('StoreType', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'stores'

class StoreType(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'store_types'
