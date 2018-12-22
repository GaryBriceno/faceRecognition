from django.db import models
from django.utils import timezone
from django.urls import reverse


class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default='Glober')
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True)
    picture = models.CharField(max_length=250, blank=True)
    country_site = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ('-first_name',)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name+", "+self.last_name

    def get_absolute_url(self):
        return reverse('people:people_detail', args=[self.slug])















