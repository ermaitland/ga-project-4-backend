from .common import BrandSerializer
from products.serializer.common import ProductSerializer

class PopulatedBrandSerializer(BrandSerializer):
    products = ProductSerializer(many=True)