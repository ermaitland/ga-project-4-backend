from django.urls import path
from .views import MyMedsList

urlpatterns = [
  path('', MyMedsList.as_view())
]