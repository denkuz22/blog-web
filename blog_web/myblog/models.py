from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
  politics = 'POL'
  tech = 'TECH'
  env = 'ENVIRONMENT'
  fin = 'FINANCE'
  category_choices = (
        (politics, 'Politics'),
        (env, 'Environment'),
        (tech, 'Tech'),
        (fin, 'Finance'),
    )
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  category = models.CharField(max_length=20,choices = category_choices,default = politics)
  def __str__(self):
      return self.title

  def get_absolute_url(self):
    return reverse("post-detail", kwargs={"pk": self.pk})
      
  
