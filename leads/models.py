from django.db import models
from django.db.models.fields import files


class Agent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)


class Lead(models.Model):    
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    age        = models.IntegerField(default=0)

# Now we need an Agent to whom the leads belong to and to do that we will introduce foreign keys
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

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





