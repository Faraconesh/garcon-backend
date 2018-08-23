from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category, Restaurant, Comment, Food, Order
from datetime import datetime
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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
    food = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'