from django.contrib.auth.models import AbstractUser
from django.db import models
import pdb

# Create your models here.
class WebUser(AbstractUser):
    gmail = models.EmailField(unique=True, blank=False, null=False)
    token = models.CharField(max_length=255, blank=True, null=True)

    #should be save
    @staticmethod
    def create_user(username, gmail, password):
        print("CREATE USER WITH: [username=", username,"gmail ", gmail," password ", password,"]")
        WebUser.objects.create(username=username, gmail=gmail, password=password)
    
    def create_api_token():
        None
