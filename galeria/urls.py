from django.urls import path
from galeria.views import inicial, imagem, buscar

urlpatterns = [
    path('', inicial, name='inicial'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar,name="buscar")
]