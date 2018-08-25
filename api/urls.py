from django.urls import path, include
from api.views import RestaurantList, CategoryList, FoodList, FoodDetails, FoodCreation, OrderCreation, OrderList, UserOrderList, OrderDetails, UserOrderDetails

urlpatterns = [
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration', include('rest_auth.registration.urls')),
    path('restaurantList', RestaurantList.as_view(), name='Restaurant List'),
    path('categoryList', CategoryList.as_view(), name='Category List'),
    path('foodList', FoodList.as_view(), name='Food List'),
    path('foodCreation', FoodCreation.as_view(), name='Food Creation'),
    path('foodDetails/<int:pk>', FoodDetails.as_view(), name='Food Details'),
    path('orderCreation', OrderCreation.as_view(), name='Order Creation'),
    path('orderList', OrderList.as_view(), name='Order List'),
    path('myOrderList', UserOrderList.as_view(), name='User Order List'),
    path('orderDetails/<int:pk>', OrderDetails.as_view(), name='Order Details'),
    path('myOrderDetails/<int:pk>', UserOrderDetails.as_view(), name='User Order List'),
]
