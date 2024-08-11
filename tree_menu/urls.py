from django.urls import path
from .views import menu_view

urlpatterns = [
    path('<str:menu_name>/', menu_view, name='menu'),
]
