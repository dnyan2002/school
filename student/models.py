from django.db import models

# Create your models here.
class Student(models.Model):
    language_choices = [
        ('', 'Select Language'),
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('R', 'R'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('Cloud', 'Cloud'),
        ('Excel', 'Excel'),
        ('Bootstrap', 'Bootstrap'),
        ('Leadership', 'Leadership'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.FileField()
    date_of_birth = models.DateField()
    skills = models.CharField(max_length=50, choices=language_choices)
    education = models.CharField(max_length=100)