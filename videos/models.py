from django.db import models
from os.path import basename
# Create your models here.
class Video(models.Model):

    """Video with source and name."""
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    introduction = models.TextField()
    source = models.URLField()
    slug = models.SlugField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = basename(self.source)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return "http://vt.cncn.win/hls/" + self.slug
