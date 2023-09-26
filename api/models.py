from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class Posts (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    userimage = models.URLField(blank=True, null=True)

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    like = models.IntegerField(default=0, null=True, blank=True)
    likeUsername = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Comments (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    userimage = models.URLField(blank=True, null=True)
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
    
class LikesComments (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.id_comment.body


    
class Historias (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id_user.username
    
class Mensajes (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_user2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='id_user2')
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.body
    
    