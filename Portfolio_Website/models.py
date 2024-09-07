from django.db import models


class ExistingModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# New model (Project) that you're adding
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    date_posted = models.DateTimeField(auto_now_add=True)
    website_url = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject