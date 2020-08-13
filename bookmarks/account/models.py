from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class Pdfs(models.Model):
    university = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.pdf.name

    objects = models.Manager()