from django.db import models

class Proj(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='profo/image/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title
