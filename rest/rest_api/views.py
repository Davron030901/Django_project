from .serializers import ProductSerializer
from  rest_framework import viewsets,permissions
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer


# Create your views here.
