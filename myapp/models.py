# myapp/models.py
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    
    # 🔴 ITO ANG IMPORTANTE: ImageField para sa pictures
    # Gagamitin nito ang MEDIA_ROOT na ni-set natin sa settings.py
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    github_link = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name