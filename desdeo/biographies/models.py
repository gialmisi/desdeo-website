from django.db import models

class Bio(models.Model):
    """Defines a model to contain biographical entries for the various team
    members.

    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        """Used to display the model on the admin site, for example.

        """
        return self.name

