from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Post(models.Model):
    judul = models.CharField(max_length=100)
    body = models.TextField()

    LIST_CATEGORY = (
        ('Jurnal', 'Jurnal'),
        ('Blog', 'Blog'),
        ('Berita', 'Berita'),
        ('Gosip', 'Gosip'),
    )
    category = models.CharField(
        max_length=100,
        choices=LIST_CATEGORY,
        default='Blog',
    )

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)
