from django.urls import path
from .views import HomeView


app_name = 'crm'

urlpatterns = [
    path('', HomeView, name='home'),
]