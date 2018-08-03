from rest_framework import serializers
from api.models import Food, Order

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = 'foods', 'submitDateTime', 'orderDateTime', 'details'