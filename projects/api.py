from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializaer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permision_clases = [permissions.AllowAny]
    serializer_class = ProjectSerializaer

