from rest_framework import viewsets

from .serializers import RecordSerializers
from .models import RecordModel

class RecordView(viewsets.ModelViewSet):
  queryset = RecordModel.objects.all()
  serializer_class = RecordSerializers
