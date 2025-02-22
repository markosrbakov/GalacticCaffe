from django.shortcuts import render
from GalacticMenu.models import Product, Event, GalerijaKafic
from django.utils import timezone
import json
import random


import json
import datetime

def index(request):
    # Земаме сите продукти
    products = Product.objects.all()

    # Ако има параметар за категорија, ги филтрираме
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(kategorija=category_filter)

    # Земаме уникатни категории
    categories = Product.objects.values_list('kategorija', flat=True).distinct()

    # Вчитување на JSON фајлот
    with open("quotes.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    quotes = data.get("quotes", [])  # Листата со мисли
    daily_quote = "Нема достапни мисли за денес."  # Дефолт ако листата е празна

    if quotes:
        today_index = datetime.date.today().toordinal() % len(quotes)
        daily_quote = quotes[today_index]

    context = {
        'products': products,
        'categories': categories,
        'daily_quote': daily_quote,  # Додадена мисла на денот
    }
    return render(request, 'index.html', context)


def product_by_category(request, category_name):
    # Филтрираме производи по категорија
    products = Product.objects.filter(kategorija=category_name)

    # Земаме уникатни категории
    categories = Product.objects.values_list('kategorija', flat=True).distinct()

    context = {
        'category': category_name,
        'products': products,
        'categories': categories,  # Додадени категории
    }
    return render(request, 'index.html', context)  # Рендерираме филтрирани продукти


def events_view(request):
    # Филтрирање на настани што се во иднина (настани после денешниот датум)
    events = Event.objects.filter(date__gte=timezone.now())  # Филтрирање по датум
    for event in events:
        event.percentage = round((event.reservations_count / 37) * 100, 2)  # Процент на резервации
    return render(request, 'events.html', {'events': events})


def gallery_view(request):
    media = GalerijaKafic.objects.all()
    return render(request, 'gallery.html', {'media': media})


def get_random_quote():
    with open("quotes.json", "r", encoding="utf-8") as f:
        data = json.load(f)  # Ова враќа речник

    all_quotes = data.get("quotes", []) + data.get("motivation_quotes", [])  # Спој ги сите мисли

    if not all_quotes:
        return "Нема достапни мисли. Додадете нови!"

    return random.choice(all_quotes)  # Бира случајна мисла


def quote_view(request):
    random_quote = get_random_quote()  # Користи ја поправената функција

    return render(request, "quote.html", {"quote": random_quote})
