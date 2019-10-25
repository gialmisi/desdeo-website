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


class AboutText(SingletonModel):
    """The main text appering on the About page.

    """
    text = models.TextField(default=None)

    def __str__(self):
        return "The main text contents"
