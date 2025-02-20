from django.contrib import admin
from django.urls import path
from GalacticMenu import views
from django.conf import settings
from django.conf.urls.static import static

from GalacticMenu.views import quote_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Патека за главната страница
    path('category/<str:category_name>/', views.product_by_category, name='product_by_category'),  # Патека за категорија
    path('events/', views.events_view, name='events'),
    path('gallery/', views.gallery_view, name='gallery'),
    path("quote/", quote_view, name="quote"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
