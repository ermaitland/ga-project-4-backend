from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .serializers.common import RequestsSerializer
from django.db import IntegrityError

from .models import Requests

class RequestsListView(APIView):
    
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