from django.urls import path

from config import settings
from . import views
from .views import product_list, product_detail
from django.conf.urls.static import static

app_name = 'falcon'

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
