from django.db import models
from django.utils import timezone 
from django.urls import reverse
from django.contrib.auth.models import  User

class Post (models.Model) :
     title = models.CharField(max_length=180)
     tech = models.CharField(max_length=180 , default = 'Tech1')
     content = models.TextField(default = 'content')
     date_posted = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     code_link=models.URLField(blank=True)
     
     def __str__(self):
           return self.title
     def get_absolute_url(self):
           return reverse('blog-detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    email= models.EmailField(default='email')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text