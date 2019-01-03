from django.urls import reverse
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 150)
    profile_picture = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manage_contacts:detail', kwargs={'pk': self.pk})

class Contact (models.Model):
    name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manage_contacts:detail', kwargs={'pk': self.person.id})