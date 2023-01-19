from django.urls import path
from .views import BrandDetailView, BrandListView, BrandSearch

urlpatterns = [
  path('', BrandListView.as_view()),
  path('<int:pk>/', BrandDetailView.as_view()),
  path('search/', BrandSearch.as_view())
]