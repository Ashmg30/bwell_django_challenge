from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import Facility, Address, Description
from .serializers import FacilitySerializer, AddressSerializer, DescriptionSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

class FacilityViewSet(ModelViewSet):
    search_fields = ['description__short_description']
    filter_backends = (filters.SearchFilter,)
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    pagination_class = StandardResultsSetPagination

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = StandardResultsSetPagination


class DescriptionViewSet(ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    pagination_class = StandardResultsSetPagination

