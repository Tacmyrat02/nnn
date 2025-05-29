from django.http import FileResponse, Http404
from .models import VPNConfig

def get_vpn_config(request, token):
    try:
        config = VPNConfig.objects.get(token=token)
        return FileResponse(config.config_file, as_attachment=True, filename=f"{config.name}.npvt")
    except VPNConfig.DoesNotExist:
        raise Http404("Konfigurasiýa tapylmady.")
