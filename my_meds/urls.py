from django.urls import path
from .views import MyMedsList, MyMedsDetailView

urlpatterns = [
  path('', MyMedsList.as_view()),
  path('<int:pk>/', MyMedsDetailView.as_view())
]