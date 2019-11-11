from django.db import models


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


class AboutDescription(SingletonModel):
    """Short description of the about page with image.

    """
    title = models.CharField(max_length=100)
    text_content = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return "About page short description"


class TeamDescription(SingletonModel):
    """Short description of the team page with image.

    """
    title = models.CharField(max_length=100)
    text_content = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return "Team page short description"


class PublicationsDescription(SingletonModel):
    """Short description of the team page with image.

    """
    title = models.CharField(max_length=100)
    text_content = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return "Publication page short description"
        
        
