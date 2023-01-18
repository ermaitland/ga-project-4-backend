from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.common import RequestsSerializer

from .models import Requests

class RequestsListView(APIView):
    def get(self, _request):
      requests = Requests.objects.all()
      serialized_requests = RequestsSerializer(requests, many=True)
      return Response(serialized_requests.data, status=status.HTTP_200_OK)