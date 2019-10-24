from django.db import models


class article(models.Model):
    """Specifies a model for a news article.

    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateField()
    last_edit = models.DateField(auto_now=True)
    contents = models.TextField()

