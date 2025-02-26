from django.urls import path
from ent_MVT.views import *

urlpatterns = [
    path('datos/<int:dni>/<int:edad>/<str:nombre>/', familia),
    path ('datos/', inicio, name='inicio')
]
