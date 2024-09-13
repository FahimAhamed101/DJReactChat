from django.urls import path
from .views import AccountViewSet, LogoutAPIView



urlpatterns = [
    path("", AccountViewSet.as_view({'get':'retrieve'})),
    path("logout/", LogoutAPIView.as_view(), name="user_logout")
    
]