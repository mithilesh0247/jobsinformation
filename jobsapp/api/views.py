from rest_framework import viewsets
from jobsapp.models import Hydjobs
from jobsapp.api.serializers import HydJobsSerializer
class HydJobsCRUDCBV(viewsets.ModelViewSet):
	serializer_class=HydJobsSerializer
	queryset=Hydjobs.objects.all()	