from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index,name='management'),
    path('chairmans/', views.chairmans,name= 'chairmans'),
    path('confirmstock', include('confirmstock.urls')),
]
