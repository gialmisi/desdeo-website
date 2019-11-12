from django.db import models
from stdimage import StdImageField


class CarouselImages(models.Model):
    """Contains the images to be displayed on the carousel.

    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = StdImageField(upload_to="images/", variations={"large": {"width": 800, "height": 600}})

    def __str__(self):
        return self.name


class Featurette(models.Model):
    """Image, title, description and view name for the featurettes displayed on
    the front page.

    """
    title = models.CharField(max_length=100)
    text_content = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    order = models.IntegerField()
    image = models.ImageField(upload_to="images/", help_text="Image should be big, preferably bigger than 400 by 600 pixels.")

    def __str__(self):
        return self.title
        
        
