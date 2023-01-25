from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from .models import FAQs
from .serializer import FAQsSerializer

class FAQsListView(APIView):
    def get(self, _request):
        faq = FAQs.objects.all()
        serialized_faq = FAQsSerializer(faq, many=True)
        return Response(serialized_faq.data, status=status.HTTP_200_OK)
            