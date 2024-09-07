from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    date_posted = models.DateTimeField(auto_now_add=True)
    website_url = models.URLField()

    def __str__(self):
        return self.title
