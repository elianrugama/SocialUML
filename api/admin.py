from django.contrib import admin

# Register your models here.

from .models import Usuario, Posts, Comments, Likes, LikesComments, Historias, Mensajes

admin.site.register(Usuario)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(LikesComments)
admin.site.register(Historias)
admin.site.register(Mensajes)
