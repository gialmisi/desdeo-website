from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import os


class OverwriteStorage(FileSystemStorage):
    """If a file name with the same name exists, remove the old file.

    """

    def get_available_name(self, name, max_length=100):
        if self.exists(name):
            os.remove(os.path.join(self.location, name))
        return name


class SingletonModel(models.Model):
    """Defines a singleton model which means, only one instance of this kind of
    model can exist in a database. Used to manage single entry data, like
    general descriptions or recurring static information. Models are used
    instead of static files since the administration page allows to easily
    modify models, so no need to juggle files around every time a typo is
    fixes.

    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Content(SingletonModel):
    """The main text appering on the About page.

    """

    contents = models.TextField(
        help_text="The main contents of the about page. Markdown is supported. "
        "Image names should follow the path '/media/images/about/'. Example: "
        "'/media/images/about/figure_name.png'."
    )

    def __str__(self):
        return "The main contents of the about page."


class Image(models.Model):
    content = models.ForeignKey(Content, models.CASCADE, related_name="images")
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="images/about", storage=OverwriteStorage()
    )

    def __str__(self):
        return self.name


class Downloadable(models.Model):
    """Contains models for files that are downloadable from the about page.

    """

    name = models.CharField(max_length=100)
    description = models.TextField(
        max_length=1000, help_text=("Short description about the file.")
    )
    file = models.FileField(help_text=("The file to be made available"))

    def __str__(self):
        return self.name


class Video(models.Model):
    """Contains a video link, a title, and a description for a video to be embedded,

    """

    name = models.CharField(
        max_length=100,
        help_text="This will also be the title used for the video.",
    )
    description = models.TextField(
        max_length=1000, help_text="Short description about the video."
    )

    url = models.URLField(
        max_length=200, help_text="URL to a video supporting embedding."
    )

    def __str__(self):
        return self.name
