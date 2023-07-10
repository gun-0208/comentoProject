from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.TextField(null=False)
    prod_category = models.TextField(null=False)
    prod_price = models.IntegerField(null=False)
    prod_quantity = models.IntegerField(null=False)
    prod_summary = models.TextField(null=False)

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image_path = models.TextField(null=False)