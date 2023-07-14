from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class Items(APIView):
    def get(self,request):
        """
        TODO: 상품 리스트 dummy 수집 및 백엔드 구성

        """
        return render(request,'shop/item_list.html')


class Item(APIView):
    '''
        TODO: 상품 상세정보 dummy 수집 및 백엔드/모델링 구성
    '''
    def get(self,request,item_id):
        return render(request,'shop/item_detail.html')

class Cart(APIView):
    def get(self,request):
        """
        TODO: 장바구니 렌더링 구현
        """
        return render(request,'shop/cart.html')
