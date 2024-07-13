from django.db import models
from .validators import validate_video_file

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', validators=[validate_video_file])

    def __str__(self):
        return self.title