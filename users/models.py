from django.db import models

# Create your models here.
    
class Address(models.Model):
    city = models.CharField(max_length=50)
    

class Country (models.Model):
    country = models.CharField(max_length=50)
    

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    age =models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False) 
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    country = models.ManyToManyField(Country, related_name='users', blank=True)

class Citizenship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='citizen')
    national_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(default="2000-01-01")

class education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
class experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    
    