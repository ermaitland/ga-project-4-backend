from django.urls import path
from .views import BrandDetailView, BrandListView

urlpatterns = [
  path('', BrandListView.as_view()),
  path('<int:pk>/', BrandDetailView.as_view())
]