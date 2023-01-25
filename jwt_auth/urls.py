from django.urls import path
from .views import RegisterView, LoginView, UserDetail, UserDetailDelete

urlpatterns = [
  path('register/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('requests/<int:pk>/', UserDetail.as_view()),
  path('myMeds/<int:pk>/', UserDetailDelete.as_view())
]