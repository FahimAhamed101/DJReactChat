"""
URL configuration for djchat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from account.views import JWTCookieTokenObtainPairView, JWTCookieTokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', JWTCookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', JWTCookieTokenRefreshView.as_view(), name='token_refresh'),

    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/schema/ui/', SpectacularSwaggerView.as_view(), name='schema-ui'),
    path("api/server/", include("server.urls")),
     path("api/account/", include("account.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
