from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class Main(APIView):
    def get(self,request):
        print("GET: main-page")
        return render(request,'Main/index.html')

class Company(APIView):
    def get(self,request):
        print("GET: aboutUs")
        return render(request,'Main/aboutUs.html')

class ContactUs(APIView):
    def get(self,request):
        print("GET: contactUs")
        return render(request,'Main/contactUs.html')