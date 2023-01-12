from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.base, name='receptes-home'),
    path('search/',views.search, name="receptes-search"),
    path('details/<str:name>/',views.details, name="receptes-details")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
