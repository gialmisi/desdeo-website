from django.db import models

import os


class Article(models.Model):
    """Specifies a model for a news article.

    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateField(help_text="The publication date.")
    contents = models.TextField(
        help_text="The textual content of the news article.  Markdown is supported. Image names should follow the path '/media/images/news/'. Example: '/media/images/news/figure_name.png'."
    )
    image = models.ImageField(
        help_text="An image to be displayed at the end of the news article.", blank=True, upload_to="images/news"
    )

    def __str__(self):
        return self.title
