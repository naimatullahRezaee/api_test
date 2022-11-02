from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.books_list, name='list-book'),
    path("", views.book_create, name='create-book'),
    path("<int:pk>", views.book),
    
]
