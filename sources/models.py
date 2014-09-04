from django.db import models

class Source(models.Model):
    MALE = 'Male'
    FEMALE = 'FEMALE'
    UNDEFINED = 'NOT SPECIFIED'
    GENDERS_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (UNDEFINED, 'UNDEFINED'),
    )
    source_url = models.TextField()
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=13,
                                      choices=GENDERS_CHOICES,
                                      default=UNDEFINED)




def matchSourceWithUser(gender=None, location=None):
    return Source.source_url(gender, location);