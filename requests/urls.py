from django.urls import path
from .views import RequestsListView, RequestCreate

urlpatterns = [
  path('', RequestsListView.as_view()),
  path('create/', RequestCreate.as_view())
]