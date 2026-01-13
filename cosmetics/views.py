from rest_framework.viewsets import ModelViewSet
from .models import Cosmetic
from .serializers import CosmeticSerializer

class CosmeticViewSet(ModelViewSet):
    queryset = Cosmetic.objects.all()
    serializer_class = CosmeticSerializer
