from rest_framework import serializers
from api.models import Food, Order
from datetime import datetime
from django.utils import timezone

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('user',)

class AdminOrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    food = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    # orderDateTime = serializers.SerializerMethodField()

    # def get_orderDateTime(self, product):
    #     # today = datetime.today()
    #     today = datetime.now(tz=timezone.utc)
    #     tomorrow = datetime.now(tz=timezone.utc)
    #     # tomorrow = datetime.today() 
    #     qs = Order.objects.filter(orderDateTime__range=(today, tomorrow))
    #     serializer = OrderSerializer(instance=qs, many=True)
    #     return serializer.data

    class Meta:
        model = Order
        fields = '__all__'
