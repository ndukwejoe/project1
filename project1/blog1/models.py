from django.db import models

# Create your models here.
class Board(models.Model):
    title=models.TextField()
    pic=models.ImageField(blank=True,upload_to='mypicture')

    def __str__(self):
        return f"{self.title}"
