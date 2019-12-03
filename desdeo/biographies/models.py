from django.db import models
from stdimage import StdImageField


class Bio(models.Model):
    """Defines a model to contain biographical entries for the various team
    members.

    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Max length 1000 characters.")
    keywords = models.CharField(max_length=100, help_text="Keywords to give a brief idea of fields of expertise")
    email = models.EmailField(max_length=100)
    image = StdImageField(upload_to="images/", variations={"thumbnail": {"width": 140, "height": 140, "crop": True}}, help_text="Image ratio should be 1:1 and size greater than 140 by 140 pixels.")

    def __str__(self):
        """Used to display the model on the admin site, for example.

        """
        return self.name

class OtherContributor(models.Model):
    """The names of the other contributors

    """
    name = models.CharField(max_length=100, help_text="Max length 100 characters.")

    def __str__(self):
        return self.name
        


