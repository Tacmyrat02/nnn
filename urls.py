from django.urls import path
from .views import get_vpn_config

urlpatterns = [
    path('sub/<uuid:token>/', get_vpn_config, name='vpn_config'),
]
