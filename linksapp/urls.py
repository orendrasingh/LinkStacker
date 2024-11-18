from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('viewlink/<int:pk>/<slug:title>/',views.viewlink,name='viewlink'),
    # path('createlink/',views.createlink,name='createlink'),
    path('',views.index,name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)