from django.db import models


class Article(models.Model):
    """Specifies a model for a news article.

    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateField()
    contents = models.TextField()

    def __str__(self):
        return self.title
