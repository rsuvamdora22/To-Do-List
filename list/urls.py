from django.urls import path
from . import views

urlpatterns = [
    path('main',views.main,name='main'),
    path('list',views.list,name='list'),
    path('details/<int:pk>',views.detail,name='details'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('history',views.history,name='history'),
    path('about',views.about,name='about')
]