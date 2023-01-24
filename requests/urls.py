from django.urls import path
from .views import RequestsListView, RequestCreate, RequestDetailView

urlpatterns = [
  path('', RequestsListView.as_view()),
  path('create/', RequestCreate.as_view()),
  path('<int:pk>/', RequestDetailView.as_view())
]