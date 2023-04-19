from .import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
   
    path('cartochka', views.Cartochka, name='Cartochka'),
    path('cartclear', views.cartclear, name='cartclear'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)