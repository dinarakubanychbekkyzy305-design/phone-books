from rest_framework.viewsets import ModelViewSet
from .models import Flower
from .serializers import FlowerSerializer

class FlowerViewSet(ModelViewSet):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer
