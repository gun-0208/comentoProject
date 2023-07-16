from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from user.models import CustomUser
from django.contrib.auth.hashers import make_password

# Create your views here.
class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self,request):
        """
        TODO: 사용자 프로필 이미지 모델 추가 및 media 저장경로 지정, 프론트 파일 업로드 기능 추가
        """
        email = request.data.get('email')
        name = request.data.get('name')
        nickname = request.data.get('nickname')
        phone = request.data.get('phone')
        address = request.data.get('address')
        password = request.data.get('password')
        is_admin = request.data.get('is_admin')
        is_employee = request.data.get('is_employee')
        is_customer = request.data.get('is_customer')

        CustomUser.objects.create(
            email=email,
            name=name,
            nickname=nickname,
            phone=phone,
            address=address,
            password=make_password(password),

        )
        # is_admin = is_admin,
        # is_employee = is_employee,
        # is_customer = is_customer

        user_test = CustomUser.objects.filter(email=email)
        print(user_test)

        return HttpResponse(status=200)

class Login(APIView):

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            return HttpResponse(status=400,data=dict(message="회원정보가 잘못 되었습니다."))

        if user.check_password(password):
            request.session['email'] = email

            return HttpResponse(status=200)

        return HttpResponse(status=400,data=dict(message="회원정보가 잘못 되었습니다."))

class Logout(APIView):
    def get(self,request):
        request.session.flush()

        return HttpResponse(status=200)


class MyPage(APIView):
    def get(self, request):
        """
        TODO : 마이페이지 구현
        """
        email = request.session.get('email',None)

        print("마이페이지 유저:" ,email)

        if email is None:
            return render(request,'user/login.html')

        return render(request, 'user/mypage.html')
