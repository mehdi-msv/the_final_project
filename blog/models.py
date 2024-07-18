from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.



class Tags(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    
    
class Categories(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null = True)
    image = models.ImageField(upload_to='blog/',default='blog/blog-img2.png')
    profile = models.ImageField(upload_to='blog/profile/',default='blog/profile/profile.jpg')
    tags = TaggableManager()
    status_type = models.TextChoices("status_type",'published unpublished')
    status = models.CharField(blank=True, choices=status_type.choices, max_length=15)
    category = models.ManyToManyField(Categories)
    login_required = models.BooleanField(default=False)
    counted_views = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-pub_date']
    def __str__(self):
        return f'{self.title} {self.id}'
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return f'{self.name} {self.email}'