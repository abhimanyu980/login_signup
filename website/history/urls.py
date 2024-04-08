from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.home, name='history'),
    path('history/<int:id>', views.delete, name='delete'),
]