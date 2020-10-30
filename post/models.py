from django.db import models

# Create your models here.


class Post(models.Model):
    caption = models.CharField(max_length=122)
    url = models.CharField(max_length=2200)
    desc = models.TextField()

    def __str__(self):
        return self.caption
