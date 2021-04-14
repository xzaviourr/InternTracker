from rest_framework import serializers
from .models import registration

class Registration_Data_Serializeer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"