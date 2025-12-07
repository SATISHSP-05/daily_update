from django.shortcuts import render

def home(request):
    products = [
        {
            "name": "Red T-Shirt",
            "price": 499,
            "description": "Comfortable cotton t-shirt",
            "image": "store/images/T_shirt.webp",  # ✅ MUST match this
        },
    ]

    return render(request, "store/home.html", {"products": products})
