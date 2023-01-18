from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category
from .serializers.common import CategorySerializer

class CategoryListView(APIView):
  
    def get(self, _request):
        category = Category.objects.all()
        serialized_category = CategorySerializer(category, many=True)
        return Response(serialized_category.data, status=status.HTTP_200_OK)
            
class CategoryDetailView(APIView):
    def get(self, _request, pk):
        category = Category.objects.get(pk=pk)
        seralized_category = CategorySerializer(category)
        return Response (seralized_category.data, status=status.HTTP_200_OK)