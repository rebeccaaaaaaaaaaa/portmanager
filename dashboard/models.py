from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import admin


class Project(models.Model):
    project_name = models.CharField('Nome do projeto', max_length=30)
    project_description = models.TextField()
    project_link = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='projects/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_description', 'project_link')

def __str__(self):
    return self.title