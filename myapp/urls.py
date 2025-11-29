
from django.urls import path
from . import views

urlpatterns = [
    # Ang path na ito ay para sa Home Page (http://yoursite.com/)
    path('', views.home, name='home'), 
]