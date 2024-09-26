from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

urlpatterns = [
    path('', views.home, name='home'),
]

# DRF ke router se automatic URLs generate karte hain
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# Existing URL patterns ke saath include kar do
urlpatterns = [
    path('', views.home, name='home'),
    # Jo bhi existing URL routes hain wo raho
    path('api/', include(router.urls)),  # API ke liye naya route
]
