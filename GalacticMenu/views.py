from django.shortcuts import render
from GalacticMenu.models import Product, Event
from django.utils import timezone

def index(request):
    # Земаме сите продукти
    products = Product.objects.all()

    # Ако има параметар за категорија, ги филтрираме
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(kategorija=category_filter)

    # Земаме уникатни категории
    categories = Product.objects.values_list('kategorija', flat=True).distinct()

    context = {
        'products': products,
        'categories': categories,  # Додадени категории
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
