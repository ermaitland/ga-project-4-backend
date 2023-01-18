from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers.common import BrandSerializer
from .models import Brand

class BrandListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get( self, _request):
        brand = Brand.objects.all()
        serialized_brand = BrandSerializer(brand, many=True)
        return Response(serialized_brand.data, status=status.HTTP_200_OK)
    def post(self, request):
        brand_to_add = BrandSerializer(data=request.data)
        try: 
            brand_to_add.is_valid()
            brand_to_add.save()
            return Response(brand_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class BrandDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self,_request, pk):
        brand = Brand.objects.get(pk=pk)
        seralized_brand = BrandSerializer(brand)
        return Response (seralized_brand.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        brand_to_edit = Brand.objects.get(pk=pk)
        # if brand_to_edit.owner != request.user:
        #       raise PermissionDenied()
        updated_brand = BrandSerializer(brand_to_edit, data=request.data)
        try:
            updated_brand.is_valid()
            updated_brand.save()
            return Response(updated_brand.data, status=status.HTTP_202_ACCEPTED)
        
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, pk):
        try:
          brand_to_delete = Brand.objects.get(pk=pk)
          # if brand_to_delete.owner != request.user:
          #     raise PermissionDenied()
          brand_to_delete.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
        except Brand.DoesNotExist:
          raise NotFound(detail="Not found")