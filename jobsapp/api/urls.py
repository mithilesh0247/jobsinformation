from django.urls import include, re_path
from rest_framework import routers
from jobsapp.api.views import HydJobsCRUDCBV
router = routers.DefaultRouter()
router.register('hydjobsinfo', HydJobsCRUDCBV)
urlpatterns = [
    re_path(r'', include(router.urls)),
]
