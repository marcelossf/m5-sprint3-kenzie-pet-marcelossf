from django.urls import path
from . import views

urlpatterns = [
    path('animals/<int:animal_id>', views.AnimalsByID.as_view()),
    path('animals/', views.AnimalView.as_view()), 
]
