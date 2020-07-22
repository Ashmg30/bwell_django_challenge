from rest_framework import routers
from .api import FacilityViewSet, AddressViewSet,DescriptionViewSet
router = routers.SimpleRouter()

router.register(r'address',AddressViewSet)
router.register(r'facility',FacilityViewSet)
router.register(r'description',DescriptionViewSet)
urlpatterns = router.urls
