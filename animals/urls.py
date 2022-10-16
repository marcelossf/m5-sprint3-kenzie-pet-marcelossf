from django.urls import path
from . import views

urlpatterns = [
    path('animals/create', views.AnimalCreateView.as_view()), #Cadastrar animais
    path('animals/<int:animal_id>', views.AnimalUpdateView.as_view()), #Atualizar animal
    path('animals/', views.AnimalView.as_view()), #Listar animais
    path('animals/id/<int:animal_id>', views.AnimalViewByID.as_view()),
    path('animals/delete/<int:animal_id>', views.AnimalDeleteView.as_view())
]
