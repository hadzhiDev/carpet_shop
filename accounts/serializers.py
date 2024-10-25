from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Employer, Employee


class SendSmsSerializer(serializers.Serializer):
    phone = PhoneNumberField()


class RegisterEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('phone', 'first_name', 'avatar', )

