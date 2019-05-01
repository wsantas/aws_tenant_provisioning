from rest_framework import serializers

from project.tenant_provisioning.models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = (
            'tenantId',
        )


