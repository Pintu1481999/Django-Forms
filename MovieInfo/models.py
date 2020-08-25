from django.db import models
import datetime
# Create your models here.
class MovieInfo(models.Model):
    movie_name = models.CharField(max_length = 100, default="")
    movie_desc = models.TextField(max_length = 500, default="")
    movie_image = models.ImageField(upload_to='images', default="")
    # created_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    # release_date = models.DateField()
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name
    # def __str__(self):
    #     return self.movie_desc