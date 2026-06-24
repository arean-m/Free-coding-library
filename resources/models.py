from django.db import models

class LearningResource(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    resource_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False) 

    def __str__(self):
        return self.title