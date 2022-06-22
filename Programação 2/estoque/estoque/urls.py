from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path('', index, name='index'),
    path('produto/', include('produto.urls', namespace='produto')),
    path('entrada/', include('notaEntrada.urls', namespace='notaEntrada')),
    path('admin/', admin.site.urls),
]
