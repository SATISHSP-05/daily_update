import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product, Cart, Banner, Order 


# ================= FETCH PRODUCTS (ONCE) =================
def fetch_products():
    if Product.objects.exists():
        return

    url = "https://dummyjson.com/products"
    data = requests.get(url).json()

    for item in data['products']:
        Product.objects.create(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            category=item['category'],
            image=item['thumbnail']
        )


# ================= SEARCH AUTOCOMPLETE API =================
def search_api(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=q)[:6]
    return JsonResponse([p.title for p in products], safe=False)


# ================= HOME PAGE =================
def home(request):
    fetch_products()

    category = request.GET.get('category')
    q = request.GET.get('q')

    products = Product.objects.all()

    if category:
        products = products.filter(category__iexact=category)

    if q:
        products = products.filter(title__icontains=q)

    categories = Product.objects.values_list('category', flat=True).distinct()
    banners = Banner.objects.all()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
        'active_category': category,
        'banners': banners
    })


# ================= AUTH =================
def register_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        return redirect('login')
    return render(request, 'register.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ================= CART =================
@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    Cart.objects.get_or_create(user=request.user, product=product)
    return redirect('cart')


@login_required
def cart_view(request):
    items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'items': items})

@login_required
def remove_from_cart(request, id):
    Cart.objects.filter(id=id, user=request.user).delete()
    return redirect('cart')


@login_required
def place_order(request):
    items = Cart.objects.filter(user=request.user)

    if not items.exists():
        return redirect('cart')

    total = sum(i.product.price * i.quantity for i in items)

    Order.objects.create(
        user=request.user,
        total_price=total
    )

    items.delete()  
    return redirect('home')


# ================= PROFILE =================
@login_required
def profile(request):
    return render(request, 'profile.html')


# ================= JWT PROFILE API =================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jwt_profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "email": user.email,
    })
