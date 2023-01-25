from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from jwt_auth.models import User

from .serializer import MyMedsSerializer, PopulatedMedsSerializer
from .models import MyMeds
from products.models import Products

class MyMedsList(APIView):

    def put(self, request):
        request.data['owner'] = request.user.id
        product_to_add = MyMedsSerializer(data=request.data)
        try:
            product_to_add.is_valid()
            product_to_add.save()
            return Response(product_to_add.data, status=status.HTTP_202_ACCEPTED)
        
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
    def get(self,_request):
      requests = MyMeds.objects.all()
      serialized_requests = PopulatedMedsSerializer(requests, many=True)
      return Response(serialized_requests.data, status=status.HTTP_200_OK)


class MyMedsDetailView(APIView):
    def delete(self, _request, pk):
        try:
          medication_to_delete = MyMeds.objects.get(pk=pk)
          medication_to_delete.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
        except MyMeds.DoesNotExist:
          raise NotFound(detail="Not found") 