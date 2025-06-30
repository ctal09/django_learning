from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    bio= models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"
    
    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Information"