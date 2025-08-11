from django.contrib import admin

from .models import *

class commentAdmininline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

@admin.register(Post)

class postAdmin(admin.ModelAdmin):
    list_display = ['id','title','enable','publish','created_time','update_time']
    inlines = [commentAdmininline, ]

class commentAdmin(admin.ModelAdmin):
    list_display = ['Post','text','created_time']

# admin.site.register(Post, postAdmin)
# admin.site.register(Comment, commentAdmin)