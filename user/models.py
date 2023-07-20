
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=24, null=False)
    nickname = models.CharField(max_length=24, null=False)
    phone = models.CharField(max_length=20, null=False)
    address = models.TextField(null=False)

    # is_admin = models.BooleanField('Is admin', default=False)
    # is_customer = models.BooleanField('Is customer', default=False)
    # is_employee = models.BooleanField('Is employee', default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)



    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "custom_user"
