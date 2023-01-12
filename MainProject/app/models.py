from django.db import models



class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_pics')
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address1 = models.TextField( )
    address2= models.TextField()
    
    
        
    def __str__(self):
        return self.name

    