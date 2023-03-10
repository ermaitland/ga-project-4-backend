from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from .serializers.common import RequestsSerializer
from .serializers.populated import PopulatedRequestSerializer
from django.db import IntegrityError
from rest_framework.exceptions import NotFound

from .models import Requests

class RequestsListView(APIView):

    def post(self, request):  
      is_staff = request.user.is_staff
      if not is_staff:
        raise PermissionDenied()
      requests = Requests.objects.all()
      serialized_requests = PopulatedRequestSerializer(requests, many=True)
      return Response(serialized_requests.data, status=status.HTTP_200_OK)

class RequestCreate(APIView):
    
    def post(self, request):
      request_to_add = RequestsSerializer(data=request.data)
      try: 
          request_to_add.is_valid()
          request_to_add.save()
          return Response(request_to_add.data, status=status.HTTP_201_CREATED)
      except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class RequestDetailView(APIView):
    def delete(self, _request, pk):
        try:
          request_to_delete = Requests.objects.get(pk=pk)
          request_to_delete.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
        except Requests.DoesNotExist:
          raise NotFound(detail="Not found") 