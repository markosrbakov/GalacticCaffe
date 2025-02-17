from django.db import models
from django.contrib.auth.models import User  # За да ја користиш корисничката таблица

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='nastani/', blank=True, null=True, default=None)
    reservations_count = models.PositiveIntegerField(default=0)  # Додај број резервации

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY_CHOICES = [
            ('Комбинации/Combos', 'Combo'),
            ('Кафе/Coffee', 'Kafe'),
            ('Чај/Tea', 'Caj'),
            ('Вода/Water', 'Water'),
            ('Цедени Сокови/Fresh-Juices', 'fres'),
            ('Сокови/Juice', 'sokovi'),
            ('Топли Напитоци/Hot Drinks', 'topli'),
            ('Пиво/Beers', 'Pivo'),
            ('Алкохол/Alchohol Drinks', 'alkohol'),
            ('Енергетски/Energetic Drinks', 'energetski'),
            ('Коктели/Cocktails', 'kokteli'),
            ('Вино/Wine', 'vino'),
            ('Шампајн/Champagne', 'sampajn'),
            ('Безалкохолни коктели/Non-alcoholic Cocktails', 'bezalkoholni'),
            ('Наргиле/Shisha', 'nargile'),
            ('Сладолед/Ice-Cream', 'sladoled'),
            ('Апетисани/Appetizers', 'Apetisani'),
            ('Шотови/Shots', 'shot'),
    ]

    name = models.CharField(max_length=100)
    opis = models.TextField(null=True, blank=True)
    cena = models.IntegerField(default=0)
    kategorija = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='produkt/', blank=True, null=True, default=None)
    kreator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  # Додадено поле за корисник

    def __str__(self):
        return self.name
