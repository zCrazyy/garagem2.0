from rest_framework.viewsets import ModelViewSet

from core.models import Carro, Categoria
from core.serializers import CategoriaSerializer, CarroSerializer, MarcaSerializer, CorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = MarcaSerializer

class CorViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CorSerializer



