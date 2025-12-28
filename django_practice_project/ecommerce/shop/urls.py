# from django.urls import path 
# from django.http import HttpResponse
# from . import views

# urlpatterns = [
#     path("",views.)
# ]



from django.urls import path
from .views import *
from .views import jwt_profile

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:id>/', add_to_cart),
    path('api/profile/', jwt_profile),
    path('api/search/', search_api),
    path('remove-cart/<int:id>/', remove_from_cart, name='remove_cart'),
    path('place-order/', place_order, name='place_order'),


]
