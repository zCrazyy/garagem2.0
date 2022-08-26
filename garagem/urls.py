from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet,CarroViewSet,CorViewSet,MarcaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

router = DefaultRouter()
router.register(r'carros', CarroViewSet)

router = DefaultRouter()
router.register(r'cores', CorViewSet)

router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
