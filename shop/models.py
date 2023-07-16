from django.db import models

from user.models import CustomUser


# Create your models here.
class Product(models.Model):
    prod_name = models.TextField(null=False)
    prod_category = models.TextField(null=False)
    prod_price = models.IntegerField(null=False)
    prod_quantity = models.IntegerField(null=False)
    prod_summary = models.TextField(null=False)
    prod_buyCount = models.IntegerField(default=0)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_path = models.TextField(null=False)


class Content(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    title = models.TextField()
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    # item_status = models.SmallIntegerField()
