from django.db import models


class SiteSettings(models.Model):
    about_us_text = models.TextField(null=True, blank=True)
    contact_us_text = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    copy_right = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=250, null=True, blank=True, default='https://instagram.com/username')
    telegram_link = models.CharField(max_length=250, null=True, blank=True, default='https://t.me/username')
    whatsapp_link = models.CharField(max_length=250, null=True, blank=True, default='https://wa.me/0123456789')


class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_send"]
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.email


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return self.question


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/service')

    def __str__(self):
        return self.title


class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    star = models.IntegerField()
    image = models.ImageField(upload_to='images/comment')

    def __str__(self):
        return self.full_name


