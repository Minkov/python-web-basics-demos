import datetime
import random

from django.shortcuts import render

cat_images = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/800px-Juvenile_Ragdoll.jpg",
    "https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg",
)

cat_names = (
    "Pepelyashka",
    "GoSho",
)


def index(request):
    index = random.randint(0, len(cat_images) - 1)
    context = {
        "cat_image": cat_images[index],
        "cat_name": cat_names[index],
        "numbers": [x + 1 for x in range(-10, 10)],
    }

    return render(request, "web/index.html", context)


def about(request):
    return render(request, "web/about.html")


def show_bootstrap(request):
    context = {
        "has_boostrap": request.GET.get("has_bootstrap", False),
    }

    return render(request, "web/bootstrap.html", context)
