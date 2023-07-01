from django.urls import path
from .views import tablero_view, verificar_view, clear_view, solucionar_view

urlpatterns = [
    path('', tablero_view, name='tablero'),
    path('comprobacion', verificar_view, name='comprobacion'),
    path('limpiar', clear_view, name='limpiar'),
    path('solucionar', solucionar_view, name='solucionar')
]