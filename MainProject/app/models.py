from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=50, null="True")
    photo = models.ImageField(upload_to='profile_pics', null='True')
    mobile = models.CharField(max_length=50, null="True")
    email = models.EmailField(max_length=50, null="True")
    address1 = models.TextField()
    address2 = models.TextField()
    # birthdate = models.DateField( null=True)

    def __str__(self):
        return self.name
