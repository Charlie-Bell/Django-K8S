from django.db import models
from django.contrib.auth.models import User



class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)

    def __str__(self): # returns name of instance object as string in terminal when print(UserInterest) or print(UserInterest__.str__()) is called.
        return self.name

class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class UserProfile(models.Model):
    # Owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    is_full_name_displayed = models.BooleanField(default=True)
    
    # Details
    bio = models.CharField(max_length=500, blank=True, null=True) # blank=True -> can be blank. null=True -> can be null.
    website = models.URLField(max_length=200, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True) # ManyToOne -> Many profiles can reference 1 persona.
    interests = models.ManyToManyField(UserInterest, blank=True)