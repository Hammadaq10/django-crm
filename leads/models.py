from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    pass


class Agent(models.Model):
    user       = models.OneToOneField(User, on_delete=CASCADE)
    # to return a string with desired output make an __str__ function
    def __str__(self):
        return self.user.email


class Lead(models.Model):    
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    age        = models.IntegerField(default=0)

# Now we need an Agent to whom the leads belong to and to do that we will introduce foreign keys
# This results in a one to many relations -----One agent can have many leads----- 
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # SOURCE_CHOICE = (
    #     ('Youtube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Linked_IN', 'Linked_IN'),    
    # )
    # phoned     = models.BooleanField(default=False)
    # source    = models.CharField(choices=SOURCE_CHOICE, max_length=1000)
    # # the blank and null makes the profile picture optional
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_file    = models.FileField(blank=True, null=True)





