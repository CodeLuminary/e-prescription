from rest_framework import serializers
from .models import Prescription, PrescriptionItem, Patient
from pharmacist.models import Drug

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = (
            "__all__"
        )

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            "__all__"
        )

class PrescriptionSerializers(serializers.ModelSerializer):
    #message = PatientSerializer
    class Meta:
        model = Prescription
        fields = (
            "__all__"
        ) #["full_name","purpose","number","age"]

class PrescriptionItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItem
        fields = (
            "__all__"
        )

class PrescriptionResultSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)
    #prescription = PrescriptionSerializers(many=False)
    class Meta:
        model = Prescription
        fields = (
            "__all__"
        ) 

class PrescriptionItemResultSerializer(serializers.ModelSerializer):
    drug_id = DrugSerializer(many=False)
    class Meta:
        model = PrescriptionItem
        fields = (
            "__all__"
        ) 