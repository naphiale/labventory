from django.urls import path
from . import views  

urlpatterns = [
    path('', views.show_main, name='show_main'),  # Pastikan ini mendefinisikan view yang benar
]
