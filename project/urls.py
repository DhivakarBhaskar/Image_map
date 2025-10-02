from django.urls import path
from app import views

urlpatterns = [
    path('', views.map, name='map'),
    path('pettai/', views.pettai, name='pettai'),
    path('ara/', views.ara, name='ara'),
    path('lake/', views.lake, name='lake'),
    path('raja/', views.raja, name='raja'),
    path('heaven/', views.heaven, name='heaven'),

]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
