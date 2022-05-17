from .models import *
from rest_framework import serializers


class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumber
        fields = ['number']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email']

class JobExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobExp
        fields = '__all__'

class AllInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllInfo
        fields = '__all__'
    