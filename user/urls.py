from django.urls import path
from . import views

urlpatterns = [
    path('registration',views.dora,name='reg'),
    path('',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
]