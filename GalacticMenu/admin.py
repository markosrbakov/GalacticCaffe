from django.contrib import admin
from GalacticMenu.models import Product,Event

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cena', 'kategorija', 'kreator')  # Подобрен приказ
    list_filter = ('kategorija', 'kreator')  # Додавање филтри

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Ако се креира нов објект
            obj.kreator = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:  # Овозможи суперкорисниците да прават измени
            return True
        return obj is None or request.user == obj.kreator

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:  # Овозможи суперкорисниците да бришат
            return True
        return obj is None or request.user == obj.kreator

admin.site.register(Product, ProductAdmin)


class EventAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Само супер админи можат да уредуваат

admin.site.register(Event, EventAdmin)