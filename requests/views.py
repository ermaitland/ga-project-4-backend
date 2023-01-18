from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .serializers.common import RequestsSerializer

from .models import Requests

class RequestsListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
      requests_to_edit = Requests.objects.all()
      serialized_requests = RequestsSerializer(requests_to_edit, many=True)
      return Response(serialized_requests.data, status=status.HTTP_200_OK)