from django.urls import path
from .views import FAQsListView

urlpatterns = [
  path('', FAQsListView.as_view())
]