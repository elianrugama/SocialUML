from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    # Agrega los campos personalizados que necesites
    # Por ejemplo:
    imagePerfil = models.ImageField(upload_to='images/perfil/', null=True, blank=True)
    imagePortada = models.ImageField(upload_to='images/portada/', null=True, blank=True)
    # Puedes agregar más campos según tus necesidades



class Posts (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    userimage = models.URLField(blank=True, null=True)

    image = models.ImageField(upload_to='images/post/', null=True, blank=True)
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
    image = models.ImageField(upload_to='images/historias/', null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    userimage = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id_user.username
    
class Mensajes (models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_user2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='id_user2')
    image = models.URLField(blank=True, null=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.body


class Grupos (models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/grupos/', null=True, blank=True)
    usuarios = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name