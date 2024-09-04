from django.shortcuts import render,redirect
from .models import Propietario,Vehiculo,Registro
# Create your views here.
def index(request):
    return render(request, 'registro_vehiculos/index.html')
def propietarios(request):
    return render(request,'registro_vehiculos/propietarios.html')
def vehiculos(request):
    return render(request, 'registro_vehiculos/vehiculos.html')
def registro(request):
    return render(request, 'registro_vehiculos/entrada_y_salida.html')
def agregar_propietario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nro_apartamento = request.POST.get('nro_apartamento')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        propietario = Propietario(nombre=nombre,nro_apartamento=nro_apartamento,telefono=telefono,email=email)
        propietario.save()
        return redirect('registro_vehiculos:propietarios')
    return render(request, 'registro_vehiculos/mostrar_propietarios.html')
def mostrar_propietario(request):
    propietarios = Propietario.objects.all()
    context = {
        'propietarios' : propietarios
    }
    return render(request, 'registro_vehiculos/mostrar_propietarios.html',context)
