from django.urls import path
from .views import notaSaidaList, notaSaidaNew, notaSaidaDelete, notaSaidaUpdate

app_name = 'notaSaida'

urlpatterns = [
    path('notaSaidaList/', notaSaidaList, name='notaSaidaList'),
    path('notaSaidaNew/', notaSaidaNew, name='notaSaidaNew'),
    path('notaSaidaDelete/<int:pk>/', notaSaidaDelete, name='notaSaidaDelete'),
    path('notaSaidaUpdate/<int:pk>/', notaSaidaUpdate, name='notaSaidaUpdate'),
]