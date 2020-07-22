from rest_framework.serializers import ModelSerializer

from .models import Facility, Address, Description

class FacilitySerializer(ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'
# Create your views here.
