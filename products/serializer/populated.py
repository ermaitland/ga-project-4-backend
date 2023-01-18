from .common import ProductSerializer
from brand.serializers.common import BrandSerializer
from jwt_auth.serializers.common import UserSerializer

class PopulatedProductSerializer(ProductSerializer):
    brand = BrandSerializer()
    owner = UserSerializer()