from .common import UserSerializer
from requests.serializers.common import RequestsSerializer

class PopulatedUserSerializer(UserSerializer):
    requests = RequestsSerializer(many=True)