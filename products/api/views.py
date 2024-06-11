from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import ProductSerializers
from ..models import Products


class ListProductView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    
class RetrieveProductView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    
class UpdateProductView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    
class DeleteProductView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    
class CreateProductView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
