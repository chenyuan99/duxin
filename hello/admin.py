from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(photos)
admin.site.register(Paperclip)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(ArticlePost)