from django.db import models


class MaterialEntry(models.Model):
    """ Material to be shared, like some data file or supplementary item to an article.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text=("Short description about the file."))

    def __str__(self):
        return self.name


class MaterialFile(models.Model):
    name = models.CharField(max_length=100, help_text="Name associated with the file.")
    file = models.FileField(help_text="File to be made available")
    material_entry = models.ForeignKey(MaterialEntry(), on_delete=models.CASCADE, related_name="files")

