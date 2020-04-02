from django.db import models
from stdimage import StdImageField


class CarouselImages(models.Model):
    """Contains the images to be displayed on the carousel.

    """

    name = models.CharField(max_length=100)
    description = models.TextField(
        max_length=1000,
        blank=True,
        help_text="Caption text to be shown on the image.",
    )
    order = models.IntegerField(
        help_text=(
            "Order of the displayed image in the carousel in ascending order. Smaller is first."
        )
    )
    image = StdImageField(
        upload_to="images/",
        variations={"large": {"width": 1200, "height": 600}},
        help_text=(
            "Image should be 1200x600 pixels, or bigger. Use a png format if "
            "the image has transparent sections."
        ),
    )

    def __str__(self):
        return self.name


class Featurette(models.Model):
    """Image, title, description and view name for the featurettes displayed on
    the front page.

    """

    title = models.CharField(max_length=100)
    text_content = models.TextField(
        max_length=1000,
        help_text=("The text to be shown next to the featurette."),
    )
    link = models.CharField(
        max_length=100,
        help_text=("The link the button on the featurettes redirects to."),
    )
    order = models.IntegerField(
        help_text=(
            "Order of the displayed featurette in ascending order. Smaller is first."
        )
    )
    image = models.ImageField(
        upload_to="images/",
        help_text=(
            "Image should be big, preferably bigger than 800 by 400 pixels, "
            "and should have an aspect ratio of 2:1. If any padding is added, "
            "it should be transparent. Use a png format."
        ),
    )

    def __str__(self):
        return self.title
