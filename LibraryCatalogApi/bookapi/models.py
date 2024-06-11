from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.




class CustomUser(AbstractUser):
      
      ROLE_CHOICES = (
            ('administrator', 'Administrator'),
            ('visitoruser', 'Visitor user'),
            ('librarian', 'Librarian'),
            ('staff', 'Staff'),
            )

      role = models.CharField(max_length=15, choices=ROLE_CHOICES)
      
      userimages = models.ImageField(null=True, default="default.jpg",upload_to='userimages/')
      first_name = models.CharField(max_length=50, null=False) 
      last_name = models.CharField(max_length=50, null=False) 
      email = models.CharField(max_length=100, null=False) 


class Genre(models.Model):
      name = models.CharField(max_length=100)

      class Meta:
            verbose_name = "Genre - category"
            verbose_name_plural = "Genres - categories"
            ordering = ['name']

      def __str__(self):
            return f'{self.name}'
      

class Author(models.Model):
      name = models.CharField(max_length=100)
      bio = models.TextField(null=True)

      class Meta:
            ordering = ['name']

      def __str__(self):
            return f'{self.name}'
      

class Publisher(models.Model):
      name = models.CharField(max_length=100)

      class Meta:
            ordering = ['name']

      def __str__(self):
            return f'{self.name}'

class Book(models.Model):
      title = models.CharField(max_length=100)
      language = models.CharField(max_length=100,default='English')
      description = models.TextField()
      price = models.IntegerField()
      genres = models.ManyToManyField(Genre, related_name='books')
      
      author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
      publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, related_name='books',null=True)
      user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,related_name='books',null=True)
      
      publication_date = models.DateTimeField(blank=True, null=True)
      published = models.BooleanField(default=False)
      availability_status = models.BooleanField(default=True)
      
      bookimage = models.ImageField(null=True, default="book.jpg",upload_to='bookimages/')
      
      
      class Meta:
            ordering = ['title']
            

      def __str__(self):
            return f'name: {self.title}, price: {self.price}'