from django.db import models
import uuid

class VPNConfig(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    config_file = models.FileField(upload_to='configs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.token})"
