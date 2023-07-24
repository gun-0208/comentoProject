from django.db import models

from user.models import CustomUser


# Create your models here.
class Product(models.Model):
    prod_name = models.TextField(null=False)
    prod_category = models.TextField(null=False)
    prod_price = models.IntegerField(null=False)
    prod_quantity = models.IntegerField(null=False)
    prod_buyCount = models.IntegerField(default=0)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_path = models.TextField(null=False)


class Content(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField()
    summary = models.TextField(null=False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=1)
    cart_status = models.SmallIntegerField(default=1)
    # 0 : 해당 상품 카트 비활성화, 1: 해당 상품 카트 활성화, 2: 해당 상품 구매 완료[비활성화].
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    carts = models.ManyToManyField(Cart)
    order_quantity = models.PositiveIntegerField(default=1)
    order_status = models.SmallIntegerField(default=0)
    name = models.CharField(max_length=24)
    phone = models.CharField(max_length=24)
    address = models.TextField()
    comment = models.TextField()
    pay_price = models.IntegerField()
#   order_not_completed:0  order_completed: 1, order_cancelled: 2
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
