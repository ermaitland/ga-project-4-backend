from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from .serializers.common import UserSerializer
from .serializers.populated import PopulatedUserSerializer
from my_meds.models import MyMeds

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({'message': 'Registration complete'}, status=status.HTTP_201_CREATED)
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied(detail="Invalid Credentials")
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail="Invalid Credentials")
        
        dt = datetime.now() + timedelta(days=7)

        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(dt.strftime('%s')), 'is_staff': user_to_login.is_staff },
            settings.SECRET_KEY,
            algorithm ='HS256'
        )
        return Response({'token': token, 'message': f"Welcome back {user_to_login.username}!"})

class UserDetail(APIView):
    def post(self, _request, pk):
        user = User.objects.get(pk=pk)
        seralized_user = PopulatedUserSerializer(user)
        return Response (seralized_user.data, status=status.HTTP_200_OK)

class UserDetailDelete(APIView):
    permission_classes = (IsAuthenticated, )
    def delete(self, request, pk):
        try:
          medication_to_delete = MyMeds.objects.get(pk=pk)
          if medication_to_delete.owner != request.user:
              raise PermissionDenied()
          medication_to_delete.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
        except MyMeds.DoesNotExist:
          raise NotFound(detail="Not found") 