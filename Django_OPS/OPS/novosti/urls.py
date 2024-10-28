from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('solve/', views.solve_quadratic, name='solve_quadratic'),
    path('trinager/', views.quadratic_trainer, name='quadratic_trainer'),
]