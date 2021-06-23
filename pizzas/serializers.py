from rest_framework_mongoengine import serializers
from .models import *
class PizzaSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class PizzaSizeSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = PizzaSize
        fields = '__all__'

class PizzaToppingSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = PizzaTopping
        fields = '__all__'