from django.urls import path

from user.views import Join, Login, MyPage, Logout

urlpatterns = [
    path("join/", Join.as_view(), name="join"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("mypage/", MyPage.as_view(), name='myPage'),
]
