from django.db import models
from django.core.validators import validate_email, ValidationError

# Create your models here.
    
class Address(models.Model):
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city
    

class Country (models.Model):
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.country
    
class Contact(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, validators=[])


def validate_age(age):
    if age <20 or age > 100:
        raise ValidationError("Age must be between 20 and 100.")

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, validators=[validate_email])
    date_joined = models.DateTimeField(auto_now_add=True)
    age =models.PositiveIntegerField(null=True, blank=True, validators=[validate_age])
    is_active = models.BooleanField(default=False) 
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    country = models.ManyToManyField(Country, related_name='users', blank=True)
    # national_id = models.CharField(Citizenship, max_length=20, unique=True, null=True, blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def clean(self):
        if self.age is not None:
           validate_age(self.age)
                
                
        if not self.email:
            raise ValidationError("Email is required.")
        if not self.first_name or not self.last_name:
            raise ValidationError("First name and last name are required.")
        if not self.address:
            raise ValidationError("Address is required.")
    
class Citizenship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='citizen')
    national_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(default="2000-01-01")
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.national_id}"
    def save(self, *args, **kwargs):
        if not self.user.age is None and (self.user.age < 20 ):
            raise ValidationError("National ID is required.")
        super().save(*args, **kwargs)


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

    
    