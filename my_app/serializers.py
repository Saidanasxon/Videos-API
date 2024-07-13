from rest_framework import serializers
from .models import * 
from .validators import validate_video_file

class VideoSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(validators=[validate_video_file])

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_file']