from django.db import models
from PIL import Image


class Tour(models.Model):
    RUSSIA = 'russia'
    THAILAND = 'thailand'
    NORWAY = 'norway'
    SOUTHAFRIC = 'southafrica'

    CHOICE_GROUP = {
        (RUSSIA, 'ru'),
        (THAILAND, 'thai'),
        (NORWAY, 'nor'),
        (SOUTHAFRIC, 'south')
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField()
    countries = models.CharField(max_length=20, choices=CHOICE_GROUP, default='')
    img = models.ImageField(default='noimage.jpg', upload_to='tour_image')

    def __str__(self):
        return f'{self.name}'