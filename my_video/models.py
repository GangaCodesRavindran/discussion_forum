from django.db import models

# Create your models here.
class MyVideo(models.Model):
    caption=models.CharField(max_length=800)
    video=models.FileField(upload_to="my_video/%y")
    def __str__(self):
        return self.caption