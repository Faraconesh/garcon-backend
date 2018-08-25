<<<<<<< HEAD
from django.urls import path, include
from api.views import RestaurantList, CategoryList, FoodList, FoodDetails, FoodCreation, OrderCreation, OrderList, UserOrderList, OrderDetails, UserOrderDetails
=======
from django.urls import path, include, re_path
from api.views import RestaurantList, FoodList, FoodDetails, FoodCreation, OrderCreation, OrderList, UserOrderList, OrderDetails, UserOrderDetails
from django.views.generic import TemplateView
>>>>>>> 0530b30b1bb54743bbcf4bf7781ea2cc675adaa4

urlpatterns = [
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),
    re_path(r'password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
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
