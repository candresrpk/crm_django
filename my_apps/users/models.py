from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Profile_Category, on_delete=models.SET_NULL, null=True, related_name='profiles')
    addres = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['id']