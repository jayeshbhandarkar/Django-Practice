
from django.contrib import admin
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contactData', views.customerDataSave, name='contactData'),
    path('add-musician/', views.add_musician, name='add_musician'),
    path('add-album/', views.add_album, name='add_album'),
    path('musician-list/', views.musician_list, name='musician_list'),
    path('album-list/', views.album_list, name='album_list'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
