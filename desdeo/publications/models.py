from django.db import models


class Publication(models.Model):
    """Defines a bibliographical entry.

    """
    authors = models.TextField(max_length=200, help_text="List of authors")
    title = models.TextField(max_length=200, help_text="Title of the publication")
    year = models.IntegerField(default=2000, help_text="Publication year. Used for sorting. NOT DISPLAYED!")
    type = models.CharField(max_length=100, default="Journal article", help_text="Type of publication, example: Journal article, conference paper")
    info = models.TextField(help_text="Example: journal name, issue, pages, publication year")
    doi_url = models.CharField(max_length=100, help_text="Link to publisher's webpage.")
    open_access_url = models.CharField(max_length=100, help_text="Optional, link to open access source.", blank=True)

    def __str__(self):
        return self.title

class OtherPublication(models.Model):
    """Defines a bibliographical entry for publications outside the DESDEO project.

    """
    authors = models.TextField(max_length=200, help_text="List of authors")
    title = models.TextField(max_length=200, help_text="Title of the publication")
    year = models.IntegerField(default=2000, help_text="Publication year. Used for sorting. NOT DISPLAYED!")
    type = models.CharField(max_length=100, default="Journal article", help_text="Type of publication, example: Journal article, conference paper")
    info = models.TextField(help_text="Example: journal name, issue, pages, publication year")
    doi_url = models.CharField(max_length=100, help_text="Link to publisher's webpage.")
    open_access_url = models.CharField(max_length=100, help_text="Optional, link to open access source.", blank=True)

    def __str__(self):
        return self.title
        

