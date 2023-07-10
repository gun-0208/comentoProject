from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class Items(APIView):
    def get(self,request):
        return render(request,'shop/item_list.html')