from django.db import models

# Create your models here.

class Contact(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField(max_length=200)
    customerSubject = models.CharField(max_length=100)
    customerMessage = models.CharField(max_length=100)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team_images/')

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()