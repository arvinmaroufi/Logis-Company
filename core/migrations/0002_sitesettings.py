# Generated by Django 5.1.5 on 2025-02-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_text', models.TextField(blank=True, null=True)),
                ('contact_us_text', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('copy_right', models.CharField(max_length=255)),
                ('instagram_link', models.CharField(blank=True, default='https://instagram.com/username', max_length=250, null=True)),
                ('telegram_link', models.CharField(blank=True, default='https://t.me/username', max_length=250, null=True)),
                ('whatsapp_link', models.CharField(blank=True, default='https://wa.me/0123456789', max_length=250, null=True)),
            ],
        ),
    ]
