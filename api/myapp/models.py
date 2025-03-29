from django.db import models

# this class defines what a single row in the database table will look like
class SampleModel(models.Model):
    title = models.CharField(max_length=200) # title will store text data
    content = models.TextField() # content will store longer text with no max required
    date = models.DateTimeField(auto_now_add=True) # date will be automatically populated

    # adding a string representation method to make model output reader friendly
    def __str__(self):
        return self.title
