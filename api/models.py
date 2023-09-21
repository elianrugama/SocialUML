from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comments (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.body
    

class Likes (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.id_post.title
    
    