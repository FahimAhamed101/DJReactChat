from django.urls import path
from rest_framework.routers import DefaultRouter
from server.views import ServerListViewSet, CategoryListViewSet

# server_router = DefaultRouter()
# server_router.register("api/servers/select", ServerListViewSet, basename='server')

urlpatterns = [
    path("select/", ServerListViewSet.as_view({'get':'list'})),
    path("category/", CategoryListViewSet.as_view({'get':'list'})),
]