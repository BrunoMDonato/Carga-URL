from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirigir_a_datos(request):
    return redirect('inicio')  # Redirige a la vista llamada 'inicio' en ent_MVT/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ent_MVT/', include('ent_MVT.urls')),
    path('', redirigir_a_datos),  # Redirige la raíz a /datos/
]
