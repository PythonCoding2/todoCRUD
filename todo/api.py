from .models import Todo
from rest_framework import viewsets, permissions
from .selializer import TodoSerializer

class TodoVeiwSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer