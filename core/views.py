from rest_framework.viewsets import ModelViewSet

from core.models import Carro, Categoria, Cor, Marca
from core.serializers import CategoriaSerializer, CarroSerializer, MarcaSerializer, CorSerializer, CarroDetailSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarroDetailSerializer
        return CarroSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer



