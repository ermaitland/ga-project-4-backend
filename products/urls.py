from django.urls import path
from .views import ProductListView, ProductDetailView, ProductSearch

urlpatterns = [
  path('', ProductListView.as_view()),
  path('<int:pk>/', ProductDetailView.as_view()),
  path('search/', ProductSearch.as_view())
]