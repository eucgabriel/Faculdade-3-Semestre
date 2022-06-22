from django.urls import path
from .views import notaEntradaList, notaEntradaNew, notaEntradaDelete, notaEntradaUpdate

app_name = 'notaEntrada'

urlpatterns = [
    path('notaEntradaList/', notaEntradaList, name='notaEntradaList'),
    path('notaEntradaNew/', notaEntradaNew, name='notaEntradaNew'),
    path('notaEntradaDelete/<int:pk>/', notaEntradaDelete, name='notaEntradaDelete'),
    path('notaEntradaUpdate/<int:pk>/', notaEntradaUpdate, name='notaEntradaUpdate'),
]