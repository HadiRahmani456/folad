from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    CATEGORY_CHOICES = (
        ('eghtesadi', 'اقتصادی'),
        ('siasi', 'سیاسی'),
        ('varzeshi', 'ورزشی'),
        ('ostani', 'استانی'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/Article/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self, ):
        return reverse('news:post_detail', args=[self.slug, self.id])

    def __str__(self, ):
        return self.title


class Slid(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/Article/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    def get_absolute_url(self, ):
        return reverse('news:slid_detail', args=[self.id])


class Messenger(models.Model):
    STATUS_CHOICES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
    )
    url = models.CharField(max_length=250)
    types = models.CharField(max_length=15, choices=STATUS_CHOICES, null=True, blank=True)


class Messenger_chat(models.Model):
    STATUS_CHOICES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
    )
    url = models.CharField(max_length=250)
    type = models.CharField(max_length=15, choices=STATUS_CHOICES)


class Video(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    CATEGORY_CHOICES = (
        ('eghtesadi', 'اقتصادی'),
        ('siasi', 'سیاسی'),
        ('varzeshi', 'ورزشی'),
        ('ostani', 'استانی'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    movie = models.FileField(upload_to='images/Article/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to='images/Article/', null=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self, ):
        return reverse('news:video_detail', args=[self.slug, self.id])

    def __str__(self, ):
        return self.title
