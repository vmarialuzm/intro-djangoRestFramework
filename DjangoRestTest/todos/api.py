from rest_framework import viewsets,permissions
from .models import Todo,TestValidation
from .serializers import TodoSerializer,TestTodoSerializer,TestValidationSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer

class TestTodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestTodoSerializer

class TestValidationViewSet(viewsets.ModelViewSet):
    queryset = TestValidation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TestValidationSerializer