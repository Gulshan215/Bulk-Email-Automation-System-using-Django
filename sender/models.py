from django.db import models

# Create your models here.
class ModelFile(models.Model):
    file = models.FileField(upload_to = 'files')
    uploaded_at = models.DateTimeField(auto_now_add=True) 

class EmailTemplate(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=400)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name