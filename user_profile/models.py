from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, default='Beginner')  # Set a default value here

    def __str__(self):
        return f'{self.name} ({self.level})'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, through='UserSkill')

class UserSkill(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Professional', 'Professional'),
        ('Expert', 'Expert'),
    ]
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

class Rpa(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Java(models.Model):
    title1 = models.CharField(max_length=50)

    def __str__(self):
        return self.title1


class Selenium(models.Model):
    title2 = models.CharField(max_length=50)

    def __str__(self):
        return self.title2


class Python(models.Model):
    title3 = models.CharField(max_length=50)

    def __str__(self):
        return self.title3

class PowerBi(models.Model):
    title4 = models.CharField(max_length=50)

    def __str__(self):
        return self.title4

class AzureDevOps(models.Model):
    title5 = models.CharField(max_length=50)

    def __str__(self):
        return self.title5


class Csharp(models.Model):
    title6 = models.CharField(max_length=50)

    def __str__(self):
        return self.title6

class Cplusplus(models.Model):
    title7 = models.CharField(max_length=50)

    def __str__(self):
        return self.title7


class Employee(models.Model):
    emp_code = models.CharField(max_length=50)
    full_name = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    java = models.ForeignKey(Java,on_delete=models.CASCADE)
    cplusplus = models.ForeignKey(Cplusplus,on_delete=models.CASCADE)
    csharp = models.ForeignKey(Csharp,on_delete=models.CASCADE)
    selenium = models.ForeignKey(Selenium,on_delete=models.CASCADE)
    python = models.ForeignKey(Python,on_delete=models.CASCADE)
    powerbi = models.ForeignKey(PowerBi,on_delete=models.CASCADE)
    rpa = models.ForeignKey(Rpa,on_delete=models.CASCADE)
    azuredevops = models.ForeignKey(AzureDevOps,on_delete=models.CASCADE)