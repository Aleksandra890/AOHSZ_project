from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.products),
    path('pv', views.prodv),
    path('pg', views.prodg), 
    path('<int:pk>', views.ProdDetailView.as_view(), name='ProdDetailView'), 
    path('addincart', views.addincart, name='addincart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)