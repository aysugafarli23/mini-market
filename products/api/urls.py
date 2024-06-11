from django.urls import path
from .views import *

app_name = 'products-api'

urlpatterns = [
    path('list/', ListProductView.as_view(), name = 'api-list'),
    path('detail/<pk>', RetrieveProductView.as_view(), name='api-detail'),
    path('update/<pk>', UpdateProductView.as_view(), name='api-update' ),
    path('delete/<pk>', DeleteProductView.as_view(), name='api-delete'),
     path('create/', CreateProductView.as_view(), name='api-create'),
]
