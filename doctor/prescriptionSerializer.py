from rest_framework import serializers
from .models import Prescription, PrescriptionItem

class PrescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = (
            "__all__"
        )

class PrescriptionItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItem
        fields = (
            "__all__"
        )