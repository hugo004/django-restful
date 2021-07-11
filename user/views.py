from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer

  
  def list(self, request, *args, **kwargs):
    '''
    list users
    '''
    return super().list(request, *args, **kwargs)

  
  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)