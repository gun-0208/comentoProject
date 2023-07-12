from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class Items(APIView):
    def get(self,request):
        return render(request,'shop/item_list.html')


class Item(APIView):
    '''
        제품 상세페이지
    '''
    def get(self,request,item_id):
        return render(request,'shop/item_detail.html')