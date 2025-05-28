from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Create a Book Database here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=500)
    publication = models.IntegerField( 
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(2025)
        ])
    isbn = models.CharField(max_length=13,
        validators=[
            RegexValidator(regex='^\\d{13}$', message='ISBN must be exactly 13 digits.')
        ])

    def __str__(self):
        return f'Book: {self.title} {self.author} {self.genre} {self.publication} {self.isbn}'
    
#Title
#Author
#Genre
#Publication Year
#ISBN (International Standard Book Number)

#Create a User Database (Optional)
class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('user', 'User'),
        ('librarian', 'Librarian'),
    ]

    email = models.EmailField(max_length=254, unique=True)  # Custom email field
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='user')

    # Adding related_name to avoid clashes with the default User model's groups and permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='literature_system_user_groups',  # Custom related_name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='literature_system_user_permissions',  # Custom related_name for user_permissions
        blank=True
    )

    def __str__(self):
        return f'User: {self.username} {self.email} {self.user_type}'