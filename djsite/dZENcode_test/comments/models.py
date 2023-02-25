from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo_file = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, default=None)
    text_file = models.FileField(upload_to='text_files/%Y/%m/%d/', blank=True, null=True, default=None)

    datetime = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None, blank=True)

    def __str__(self):
        return self.body