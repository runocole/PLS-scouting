from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/') 
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

