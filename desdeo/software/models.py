from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

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
    contents = models.TextField(help_text="The main contents of the software page. Markdown is supported. "
                                "Image names should follow the path '/media/images/about/'. Example: "
                                "'/media/images/software/figure_name.png'.")

    def __str__(self):
        return "The main contents of the software page."


class Image(models.Model):
    content = models.ForeignKey(Content, models.CASCADE, related_name="images")
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="images/software",
        storage=OverwriteStorage())

    def __str__(self):
        return self.name
