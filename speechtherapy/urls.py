from django.urls import path,include
from speechtherapy.views import *

urlpatterns = [
    path('', home, name='home'),
    path('start-therapy/', start_therapy, name='start-therapy'),
]
