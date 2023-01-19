from django.urls import path
from .views import RegisterView, LoginView, UserDetail

urlpatterns = [
  path('register/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('<int:pk>/', UserDetail.as_view())
]