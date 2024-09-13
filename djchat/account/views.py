from django.conf import settings
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer, CustomTokenObtainPairSerializer, JWTCookieTokenRefreshSeializer
from .schema import account_docs
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Create your views here.


class LogoutAPIView(APIView):
    def post(self, request, format=None):
        response =  Response("Successfully Logged Out", status=200)
        response.set_cookie("access", "", expires=0)
        response.set_cookie("refresh", "", expires=0)
        return response

class AccountViewSet(viewsets.ViewSet):

    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    @account_docs
    def retrieve(self, request, *args, **kwargs):
        userId = request.query_params.get('userId', None)
        if userId is not None:
            try:
                account = self.queryset.get(id=userId)
                serializer = AccountSerializer(account)
                return Response(serializer.data)
            except Account.DoesNotExist:
                return Response({"error": "userId doesn't exists"}, status=400)
        else:
            return Response({"error": "userId parameter is required"}, status=400)


class JWTSetCookieMixin:
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"],
                response.data['refresh'],
                max_age=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                httponly=True,
                samesite=settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"]
            )
        if response.data.get("access"):
            response.set_cookie(
                settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"],
                response.data['access'],
                max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                httponly=True,
                samesite=settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"]
            )
            del response.data["access"]

        return super().finalize_response(request, response, *args, **kwargs)
    
class JWTCookieTokenObtainPairView(JWTSetCookieMixin, TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class JWTCookieTokenRefreshView(JWTSetCookieMixin, TokenRefreshView):
    serializer_class = JWTCookieTokenRefreshSeializer