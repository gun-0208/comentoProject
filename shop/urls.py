from django.urls import path

from shop.views import Items

urlpatterns = [
    path("",Items.as_view(), name="item_list")
]
