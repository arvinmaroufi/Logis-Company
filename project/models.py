from django.db import models


def image_directory_path(instance, filename):
    project_title = instance.project.title
    return f'images/projects/{project_title}/{filename}'


class Project(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='images/projects', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path)

    def __str__(self):
        return self.project.title
