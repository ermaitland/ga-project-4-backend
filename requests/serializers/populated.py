from .common import RequestsSerializer
from products.serializer.common import ProductSerializer

class PopulatedRequestSerializer(RequestsSerializer):
    products = ProductSerializer()