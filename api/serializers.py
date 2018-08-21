from rest_framework import serializers
from api.models import Category, Restaurant, Comment, Food, Order
from datetime import datetime
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)
    restaurant = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Food
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('user',)

class AdminOrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    food = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'
