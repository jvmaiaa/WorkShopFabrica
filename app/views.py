from rest_framework import viewsets
from app.models import ToDo
from app.serializers import ToDoSerializer
 
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
