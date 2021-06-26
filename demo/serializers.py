from  .models import RecordModel
from rest_framework import serializers

class RecordSerializers(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = RecordModel
    fields = '__all__'