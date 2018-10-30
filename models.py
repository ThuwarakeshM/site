from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=25, blank=False, null=False)

    job_title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name