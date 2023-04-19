from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news),
    path('SME_O_NAS', views.sme),
    path('create', views.add),
    path('<int:pk>', views.NewsDetailView.as_view(), name='NewsDetailView'),
    path('<int:pk>/Update', views.NewsUpdate.as_view(), name='NewsUpdate'),
    path('<int:pk>/Delete', views.NewsDelete.as_view(), name='NewsDelete'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
