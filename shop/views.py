from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from shop.models import Product, Cart
from user.models import CustomUser


# Create your views here.
class Items(APIView):
    def get(self, request):
        """
        TODO: 상품 리스트 dummy 수집 및 백엔드 구성 / pagination이용하면 끌어올 데이터 수 제한

        """
        items = Product.objects.all.order_by('-prod_buyCount')

        return render(request, 'shop/item_list.html', context={'items': items})


class Item(APIView):
    '''
        TODO: 상품 상세정보 dummy 수집 및 백엔드/모델링 구성
    '''

    def get(self, request, item_id):
        item = get_object_or_404(Product, pk=item_id)

        return render(request, 'shop/item_detail.html', context={'item': item})


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
        item_id = request.data.get('item_id')

        print(item_id)

        if email is None:
            return render(request, 'user/login.html')

        user = CustomUser.objects.filter(email=email).first()
        item = Product.objects.filter(id=item_id).first()
        cart = Cart.objects.filter(user=user, item=item).first()
        print(cart)
        if item is None:
            return HttpResponse(status=400)

        if cart is not None:
            # return HttpResponse(status=400, msg=dict(msg="장바구니에 추가 되어있습니다."))
            return HttpResponse(status=400)

        Cart.objects.create(user=user, item=item).save()

        return HttpResponse(status=200)

    def delete(self, request, item_id):
        """
        TODO: delete cart_item
        """
        pass

class Order(APIView):
    def post(self,request):
        """
        TODO: order 기능 구현
        """
        pass