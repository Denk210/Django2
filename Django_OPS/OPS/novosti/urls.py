from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('solve/', views.solve_quadratic, name='solve_quadratic'),
    path('trinager/', views.quadratic_trainer, name='quadratic_trainer'),
    path('category/<int:category_id>/', views.news_by_category, name='news_by_category'),
    path('tag/<int:tag_id>/', views.news_by_tag, name='news_by_tag'),
]