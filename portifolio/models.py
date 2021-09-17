from django.db import models

class Project(models.Model):
    project_name = models.CharField('Nome do projeto', max_length=30)
    project_description = models.TextField()
    project_link = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='projects/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


