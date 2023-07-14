from django.shortcuts import render
from rest_framework.views import APIView

from user.models import CustomUser


# Create your views here.
class Main(APIView):
    def get(self,request):
        """
            TODO: 메인페이지 유저 프로필 사진 렌더링
        """

        print("GET: main-page")
        email = request.session.get('email',None)
        print("session: ", email)

        if email is None:
            return render(request,'Main/index.html')

        user = CustomUser.objects.filter(email=email).first()
        return render(request,'Main/index.html',context={'user':user})

class Company(APIView):
    def get(self,request):
        """
        TODO: 회사소개 페이지 구현

        """
        print("GET: aboutUs")
        return render(request,'Main/aboutUs.html')

class ContactUs(APIView):
    def get(self,request):
        """
        TODO: 문의 페이지 구현

        """
        print("GET: contactUs")
        return render(request,'Main/contactUs.html')