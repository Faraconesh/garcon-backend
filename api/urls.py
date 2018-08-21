from django.urls import path, include
from api.views import RestaurantList, FoodList, FoodDetails, FoodCreation, OrderList, OrderDetails, OrderCreation

urlpatterns = [
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration', include('rest_auth.registration.urls')),
    path('restaurantList', RestaurantList.as_view(), name='Restaurant List'),
    path('foodList', FoodList.as_view(), name='Food List'),
    path('foodCreation', FoodCreation.as_view(), name='Food Creation'),
    path('foodDetails/<int:pk>', FoodDetails.as_view(), name='Food Details'),
    path('orderList', OrderList.as_view(), name='Order List'),
    path('orderCreation', OrderCreation.as_view(), name='Order Creation'),
    path('orderDetails/<int:pk>', OrderDetails.as_view(), name='Order Details'),
]
