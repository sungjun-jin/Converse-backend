from django.db      import models

from product.models import Product,Size,Color
from account.models import User

class Cart(models.Model):
    quantity = models.PositiveIntegerField(default = 0)
    product  = models.ForeignKey('product.Product', on_delete = models.SET_NULL, null = True)
    size     = models.ForeignKey('product.Size', on_delete = models.SET_NULL, null = True)
    user     = models.ForeignKey('account.User', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'carts'

