from django.urls import path
from ent_MVT.views import *

urlpatterns = [
    path ('datos/<dni>,<edad>,<nombre>', familia),
    path ('datos/', inicio)
]
