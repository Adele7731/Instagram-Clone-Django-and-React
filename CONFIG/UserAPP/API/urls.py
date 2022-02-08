
from django.urls import path
from .views import UserFollowersAPIView,UserFollowingAPIView,UserProfileAPIView

app_name="user"
urlpatterns = [
    path('followers/<str:user__username>', UserFollowersAPIView.as_view(),name="url_followers"),     # Kullanıcının takipçileri
    path('followings/<str:user__username>', UserFollowingAPIView.as_view(),name="url_followings"),   # Kullanıcının takip ettikleri
    path('<str:user__username>', UserProfileAPIView.as_view(), name="url_user"),                     # Kullanıcının profil bilgileri
]
