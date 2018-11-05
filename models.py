from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=25, blank=False, null=False)

    job_title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=50)
    section = models.ManyToManyField(Section)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=180)
    pubdate = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title