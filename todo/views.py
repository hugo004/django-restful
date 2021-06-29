from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action


from .models import Todo
from .serializers import TodoSerialzer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  
  serializer_class = TodoSerialzer
  permission_classes = [permissions.IsAdminUser]

  def list(self, request, pk=None):
    '''
    list todos
    '''
    return super().list(request, pk)

  
  def create(self, request, pk=None):
    return super().create(request, pk)
    

  def retrieve(self, request, pk=None):
    return super().retrieve(request, pk)

  
  def update(self, request, pk=None):
    return super().update(request, pk)

  
  def partial_update(self, request, pk=None):
    return super().partial_update(request, pk)


  def destroy(self, request, pk=None):
    return super().destroy(request, pk)

  
  

  # # @action(detail=False, methods=['get'])
  # def get(self, request, pk=None) -> Response:
  #   '''
  #   List all todo items
  #   '''

  #   todos = self.queryset.filter(user = request.user.id)
  #   serialzer = self.serializer_class(todos, many=True)

  #   return Response(serialzer.data, status=status.HTTP_200_OK)

  
  # # @action(detail=False, methods=['post'])
  # def post(self, request, pk=None) -> Response:
  #   '''
  #   Create todo
  #   '''
  #   data = {
  #     'task': request.data.get('task'),
  #     'completed': request.data.get('completed'),
  #     # 'user': request.user.id
  #   }
  #   serializer = self.serializer_class(data=data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


