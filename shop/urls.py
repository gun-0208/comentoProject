from django.urls import path

from shop.views import Items, Item, UserCart, Order

urlpatterns = [
    path("",Items.as_view(), name="item_list"),
    path("item/<int:item_id>", Item.as_view(), name="item_detail"),
    path("cart/",UserCart.as_view(), name="cart"),
    path("order/",Order.as_view(), name="order"),
]
