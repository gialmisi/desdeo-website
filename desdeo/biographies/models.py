from django.db import models
from stdimage import StdImageField


class Bio(models.Model):
    """Defines a model to contain biographical entries for the various team
    members.

    """
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,
                               help_text=("Used to order the profiles shown.")
    )
    order = models.IntegerField(default=1,
                                help_text=("Used to override the surname ordering. Orders the "
                                "profiles shown in ascending order, smaller is first.")
    )
    description = models.TextField(max_length=1000, help_text="Max length 1000 characters.")
    keywords = models.CharField(max_length=100, help_text="Keywords to give a brief idea of fields of expertise")
    email = models.EmailField(max_length=100)
    image = StdImageField(upload_to="images/",
                          variations={
                              "thumbnail": {"width": 140, "height": 140, "crop": True}},
                          help_text=("Image ratio should be 1:1 and size greater than 140 by 140 pixels.")
    )

    def __str__(self):
        """Used to display the model on the admin site, for example.

        """
        return f"{self.first_name} {self.surname}"

class OtherContributor(models.Model):
    """The names of the other contributors

    """
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100,
                               help_text=("Used to order the names shown.")
    )

    def __str__(self):
        return f"{self.first_name} {self.surname}"
        


