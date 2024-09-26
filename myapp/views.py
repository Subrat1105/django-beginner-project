from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

from rest_framework import viewsets
from .models import Product
from myapp.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer