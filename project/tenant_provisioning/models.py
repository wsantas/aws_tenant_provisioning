from django.db import models


class Tenant(models.Model):
    tenantId = models.TextField(default="null")
