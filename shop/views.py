from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from shop.models import Product, Cart
from user.models import CustomUser
import re

# Create your views here.
class Items(APIView):
    def get(self, request):
        """
        TODO: 상품 리스트 dummy 수집 및 백엔드 구성 / pagination이용하면 끌어올 데이터 수 제한

        """
        item_list = Product.objects.all()
        print(item_list)

        return render(request, 'shop/item_list.html', context={'item_list': item_list})


class Item(APIView):
    '''
        TODO: 상품 상세정보 dummy 수집 및 백엔드/모델링 구성
    '''

    def get(self, request, item_id):
        item = get_object_or_404(Product, pk=item_id)

        email = request.session.get('email',None)
        user = None

        if email is not None:
            user = CustomUser.objects.filter(email=email).first()

        price = ''
        for idx, ele in enumerate(str(item.prod_price)[::-1]):
            idx += 1
            price += ele
            if idx % 3 == 0 and idx != len(str(item.prod_price)):
                price += ','
        price = price[::-1]


        return render(request, 'shop/item_detail.html', context={'item': item,'price':price,'user':user})


class UserCart(APIView):
    def get(self, request):
        """
        TODO: 장바구니 목록 렌더링 구현
        """
        email = request.session.get('email',None)
        print(email)
        
        if email is None:
            return render(request, 'user/login.html')

        user = CustomUser.objects.filter(email=email).first()

        cart_items = user.cart_set.all()

        return render(request, 'shop/cart.html', context={'cart_items':cart_items})

    def post(self, request):
        """
        TODO: add cart_item
        """
        email = request.session.get('email', None)
        item_id = request.data.get('prod_id')

        print(item_id)
        print(email)

        if email is None:
            return HttpResponse(status=400)

        user = CustomUser.objects.filter(email=email).first()
        item = Product.objects.filter(id=item_id).first()
        cart = Cart.objects.filter(user=user, item=item).first()
        print(cart)

        if cart is not None:
            return HttpResponse(status=400)

        Cart.objects.create(user=user, item=item).save()

        return HttpResponse(status=200)

    def delete(self, request, item_id):
        """
        TODO: delete cart_item
        """
        pass

class Order(APIView):

    def get(self,request):
        """TODO: 주문내역 조회 구현"""


        pass


    def post(self,request):
        """
        TODO: order 기능 구현
        """
        pass

    def delete(self,request):
        """
        TODO: 주문취소 기능 구현

        """
        pass
