from django.urls import path

from shop.views import Items, Item

urlpatterns = [
    path("",Items.as_view(), name="item_list"),
    path("item/<int:item_id>", Item.as_view(), name="item_detail")
]
