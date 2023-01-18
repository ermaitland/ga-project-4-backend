from django.urls import path
from .views import RequestsListView

urlpatterns = [
  path('', RequestsListView.as_view())
]