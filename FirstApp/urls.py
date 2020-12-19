from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='FirstApp-index'),
    path('projects/', views.projects, name='FirstApp-projects'),
    path('projects/calculator/', views.calculator_project, name='FirstApp-projects-calculator'),
]
