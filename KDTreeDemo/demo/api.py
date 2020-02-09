from demo.models import Demo_model
from rest_framework import viewsets,permissions

from .serializers import DemoSerializer

class DemoViewSet(viewsets.ModelViewSet):
    queryset = Demo_model.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class = DemoSerializer