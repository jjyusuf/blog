from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    published = models.CharField(choices=(('Y', 'Yes'), ('N', 'No')), max_length=32, default='N')
    promoted = models.CharField(choices=(('Y', 'Yes'), ('N', 'No')), max_length=32, default='N')
    comments = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
