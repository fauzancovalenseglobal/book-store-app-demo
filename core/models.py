from django.db import models

# Create your models here.

class Author(models.Model):
    """This model stores the data into Author table in db"""

    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Author"   
        verbose_name_plural = "Authors" 

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    """This model stores the data into Author table in db"""

    title = models.CharField(max_length=200, verbose_name="Title of book")
    authors = models.ForeignKey("core.author", on_delete=models.CASCADE, related_name="author_book", blank=True, null=True) 
    description = models.TextField(verbose_name="Description of book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Book"   
        verbose_name_plural = "Books" 

    def __str__(self) -> str:
        return self.title
    
