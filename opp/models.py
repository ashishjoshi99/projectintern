from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(default="Username1", max_length=256)
<<<<<<< HEAD
    is_Organisation = models.BooleanField(default=False)
=======
>>>>>>> 6d2c55321ddd1f690752066621931cbe2021222a

    def __str__(self):
        return self.name
