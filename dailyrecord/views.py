from rest_framework import viewsets

from .models import DailyRecord
from .serializers import DailyRecordSerializer

class DailyRecordViewSet(viewsets.ModelViewSet):
  queryset = DailyRecord.objects.all()
  serializer_class = DailyRecordSerializer
