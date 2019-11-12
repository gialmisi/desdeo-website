from django.db import models


class BlogContent(models.Model):
    """A model to represent a blog post with main contents defined in a
    markdown format.

    """
    author = models.CharField(max_length=100)
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    contents = models.TextField()

    def __str__(self):
        return self.title
