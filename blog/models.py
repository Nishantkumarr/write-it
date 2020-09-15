from django.db import models
from django.utils import timezone 
from django.urls import reverse
from django.contrib.auth.models import  User
from djrichtextfield.models import RichTextField

class Post (models.Model) :
      title = models.CharField(max_length=180)
      #choice feild code 
      class Tech (models.TextChoices):
            PYTHON = 'Python' , "Python"
            JAVASCRIPT = 'Javascript', "Javascript"
            JAVA = 'Java' ,"Java"
            PHP='Php',"Php"
            HTML = 'Html',"Html"
            DSA='Dsa',"Dsa"
            CSS = 'Css',"Css"
            BOOTSTRAP='Bootstrap', "Bootstrap"
            NODEJS ='Node.js' ,"Node.js"
            ANGULAR='Angular',"Angular"
            REACT='React',"React"
            FLUTTER='Flutter',"Flutter"
      
      tech = models.CharField(max_length=180 ,choices=Tech.choices, default = 'Tech-Used')
      para_1 = RichTextField(default = 'content')
      date_posted = models.DateTimeField(default=timezone.now)
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      links=models.URLField(blank=True)
      
      def __str__(self):
            return self.title
      def get_absolute_url(self):
            return reverse('blog-detail',kwargs={'pk':self.pk})


class Comment(models.Model):
      post = models.ForeignKey('blog.Post', related_name='comments' , on_delete=models.CASCADE)
      name = models.CharField(max_length=200)
      comment = RichTextField()
      email= models.EmailField(default='email')
      created_date = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.text