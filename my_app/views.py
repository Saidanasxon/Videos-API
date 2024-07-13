from .serializers import *
from .models import *
from .permissions import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [CustomPermission]
    authentication_classes = [TokenAuthentication, SessionAuthentication]