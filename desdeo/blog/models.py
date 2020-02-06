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


#class Content(SingletonModel):
#    """The main text appering on the About page.
#
#    """
#    contents = models.TextField(help_text="The main contents of the software page. Markdown is supported. "
#                                "Image names should follow the path '/media/images/software/'. Example: "
#                                "'/media/images/software/figure_name.png'.")
#
#    def __str__(self):
#        return "The main contents of the software page."


class BlogContent(models.Model):
    """A model to represent a blog post with main contents defined in a
    markdown format.

    """
    author = models.CharField(max_length=100)
    pub_date = models.DateField(help_text="Publication date")
    title = models.CharField(max_length=200)
    contents = models.TextField(help_text=("The contents of the blog post. Markdown is supported. Image "
        "names should follow the path 'media/images/blog/'. "
        "Example: '/media/images/blog/figure_name.png"))

    def __str__(self):
        return self.title


class Image(models.Model):
    content = models.ForeignKey(BlogContent, models.CASCADE, related_name="images")
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="images/blog",
        storage=OverwriteStorage())

    def __str__(self):
        return self.name
