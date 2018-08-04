from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser


from api.models import Food, Order
from api.serializers import FoodSerializer, OrderSerializer, AdminOrderSerializer

# Create your views here.


class FoodList(mixins.ListModelMixin,
               generics.GenericAPIView):
    queryset = Food.objects.all()
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
    queryset = Order.objects.all()
    serializer_class = AdminOrderSerializer

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
    authentication_classes = (
        TokenAuthentication, SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    queryset = Order.objects.all()
    serializer_class = AdminOrderSerializer
