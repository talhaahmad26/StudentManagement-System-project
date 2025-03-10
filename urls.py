from django.urls import path
from .import views

urlpatterns = [
    path('', views.pakistan,name='pakistan'),
    path('<int:id>', views.view_student,name= 'view_student'),
    path('add/', views.add,name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
