from django.db import models


class BibEntry(models.Model):
    """Defines a bibliographical entry.

    """
    authors = models.TextField(max_length=200)
    title = models.TextField(max_length=200)
    journal_title = models.CharField(max_length=200)
    volume_and_issue = models.CharField(max_length=100)
    pages = models.CharField(max_length=100)
    year = models.IntegerField(default=2000)
    doi_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
        

