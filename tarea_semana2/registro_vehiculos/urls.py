from django.urls import path
from . import views
app_name='registro_vehiculos'
urlpatterns = [
    path('',views.index,name='index'),
    path('propietarios/', views.propietarios, name='propietarios'),
    path('agregar/', views.agregar_propietario, name='agregar_propietario'),
    path('propietarios/mostrar_propietarios', views.mostrar_propietario, name='mostar_propietarios')
]