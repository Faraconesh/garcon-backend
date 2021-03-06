from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import OrderingFilter

from django.db.models import Prefetch

from api.models import Restaurant, Category, Food, Order
from api.serializers import RestaurantSerializer, CategorySerializer, FoodSerializer, OrderSerializer, AdminOrderSerializer

# Create your views here.

class RestaurantList(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Restaurant.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('userWeight', 'customWeight',)
    serializer_class = RestaurantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryList(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FoodList(mixins.ListModelMixin,
               generics.GenericAPIView):
    queryset = Food.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('userWeight', 'customWeight',)
    serializer_class = FoodSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FoodCreation(mixins.CreateModelMixin,
                   generics.GenericAPIView):

    authentication_classes = (
        TokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FoodDetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OrderList(mixins.ListModelMixin,
                generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('submitDateTime', 'orderDateTime', 'id')
    serializer_class = AdminOrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class UserOrderList(mixins.ListModelMixin,
                generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('submitDateTime', 'orderDateTime', 'id')
    serializer_class = AdminOrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderCreation(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    authentication_classes = (
        TokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderDetails(generics.ListAPIView,
                   generics.UpdateAPIView,
                   generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    queryset = Order.objects.all()
    serializer_class = AdminOrderSerializer

class UserOrderDetails(mixins.RetrieveModelMixin,
                   generics.UpdateAPIView,
                   generics.DestroyAPIView,
                   generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('submitDateTime', 'orderDateTime', 'id')
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        order = Order.objects.filter(id=instance.id).first()
        food = order.food
        order_count = food.values('userWeight').first()['userWeight']
        food.update(userWeight=order_count-1)
        restaurant_id = food.values('restaurant').first()['restaurant']
        restaurant_instance = Restaurant.objects.filter(id=restaurant_id)
        restaurant_count = restaurant_instance.values('userWeight').first()['userWeight']
        restaurant_instance.update(userWeight=restaurant_count-1)
        restaurant_count = restaurant_instance.values('userWeight').first()['userWeight']
        instance.delete()