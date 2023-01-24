from .common import UserSerializer
from requests.serializers.common import RequestsSerializer
from my_meds.serializer import PopulatedMedsSerializer

class PopulatedUserSerializer(UserSerializer):
    requests = RequestsSerializer(many=True)
    my_meds = PopulatedMedsSerializer(many=True)