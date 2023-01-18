from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category
from .serializers.common import CategorySerializer

class CategoryListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        category = Category.objects.all()
        serialized_category = CategorySerializer(category, many=True)
        return Response(serialized_category.data, status=status.HTTP_200_OK)

    def post(self, request):
        category_to_add = CategorySerializer(data=request.data)
        try:
            category_to_add.is_valid()
            category_to_add.save()
            return Response(category_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
class CategoryDetailView(APIView):
    def get(self, _request, pk):
        category = Category.objects.get(pk=pk)
        seralized_category = CategorySerializer(category)
        return Response (seralized_category.data, status=status.HTTP_200_OK)