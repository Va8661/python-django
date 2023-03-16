from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi, name='home-page' ),
     path('book_appointment/', views.book_appointment, name='book_appointment'),
]