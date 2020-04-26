from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 30)

    class Meta:
        db_table = 'categories'

class Group(models.Model):
    name     = models.CharField(max_length = 40)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'groups'

class Product(models.Model):
    code          = models.CharField(max_length = 45)
    name          = models.CharField(max_length = 200)
    price         = models.PositiveIntegerField(default = 0)
    gender        = models.CharField(max_length = 45)
    color_name    = models.CharField(max_length = 45)
    silhouette    = models.ForeignKey('Silhouette', on_delete = models.SET_NULL, null = True)
    category      = models.ForeignKey('Category', on_delete = models.SET_NULL, null = True)
    group         = models.ForeignKey('Group', on_delete = models.SET_NULL, null = True)
    detail        = models.ForeignKey('Detail', on_delete = models.SET_NULL, null = True)
    product_size  = models.ManyToManyField('Size', through = 'ProductSize')
    product_color = models.ManyToManyField('Color', through = 'ProductColor')

    class Meta:
        db_table = 'products'

class Detail(models.Model):
    summary     = models.CharField(max_length = 500)
    size_img    = models.URLField(max_length = 2000, null = True)
    description = models.TextField()
    desc_img    = models.URLField(max_length = 2000)
    information = models.TextField()

    class Meta:
        db_table = 'details'

class Series(models.Model):
    code    = models.CharField(max_length = 500, null = True)
    image   = models.URLField(max_length = 2000, null = True)
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'series'

class Media(models.Model):
    media_url = models.URLField(max_length = 2000)
    product   = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'medias'

class Silhouette(models.Model):
    name = models.CharField(max_length = 10)

    class Meta:
        db_table = 'silhouettes'

class Size(models.Model):
    size = models.CharField(max_length = 100)

    class Meta:
        db_table = 'sizes'

class Color(models.Model):
    color_code = models.CharField(max_length = 50, null = True)
    color_name = models.CharField(max_length = 50, null = True)

    class Meta:
        db_table = 'colors'

class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)
    size    = models.ForeignKey('Size', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'products_sizes'

class ProductColor(models.Model):
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)
    color   = models.ForeignKey('Color', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'products_colors'
