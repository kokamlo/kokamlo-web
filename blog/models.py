from django.db import models

# Create your models here.
class bloog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()
    #image = models.ImageField(upload_to='##profo/image/')
    #url = models.URLField(blank=True)
    def __str__(self):
        return self.title
