from .common import ProductSerializer
from brand.serializers.common import BrandSerializer
from jwt_auth.serializers.common import UserSerializer
from category.serializers.common import CategorySerializer

class PopulatedProductSerializer(ProductSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    owner = UserSerializer()