from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    publish = models.DateField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=False)
    def __str__(self):
        # return self.title
        return '{}- {}'.format(self.pk,self.title)
class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)