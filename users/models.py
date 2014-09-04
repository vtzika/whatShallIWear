from django.db import models

class User(models.Model):
    MALE = 'Male'
    FEMALE = 'FEMALE'
    UNDEFINED = 'NOT SPECIFIED'
    GENDERS_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (UNDEFINED, 'UNDEFINED'),
    )
    user_id = models.CharField(max_length=50)
    place = models.CharField(max_length=200)
    gender = models.CharField(max_length=13,
                                      choices=GENDERS_CHOICES,
                                      default=UNDEFINED)


