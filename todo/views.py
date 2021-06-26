from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Todo
from .serializers import TodoSerialzer

# Create your views here.
class TodoListView(APIView):
  permission_classes = [permissions.IsAdminUser]

  def get(self, request, *args, **kwargs) -> Response:
    '''
    List all todo items
    '''
    todos = Todo.objects.filter(user = request.user.id)
    serialzer = TodoSerialzer(todos, many=True)

    return Response(serialzer.data, status=status.HTTP_200_OK)

  
  def post(self, request, *args, **kwargs) -> Response:
    '''
    Create todo
    '''
    data = {
      'task': request.data.get('task'),
      'completed': request.data.get('completed'),
      'user': request.user.id
    }
    serializer = TodoSerialzer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


