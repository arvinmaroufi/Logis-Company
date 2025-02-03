from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    ("draft", "Draft"),
    ("published", "Published"),
)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/articles', blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])

    def __str__(self):
        return self.title
