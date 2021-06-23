from django.urls import path
from .views import ResourceAPIView, GetListView,index
from .models import *
from .serializers import *
urlpatterns = [
    path('',index),
    path('pizza/<str:pk>', ResourceAPIView.as_view(
        model = Pizza,
        resource_serializer = PizzaSerializer
    )),
    path('pizza-size/<str:pk>', ResourceAPIView.as_view(
        model = PizzaSize,
        resource_serializer = PizzaSizeSerializer
    )),
    path('pizza-topping/<str:pk>', ResourceAPIView.as_view(
        model = PizzaTopping,
        resource_serializer = PizzaToppingSerializer
    )),
    path('pizza-list/<str:page>',GetListView.as_view(
        model = Pizza,
        resource_serializer = PizzaSerializer
    ))
]