from django.db import models
from .validators import validate_file_type, validate_file_size
# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_id(pk: int):
        return User.objects.get(pk=pk)

    @staticmethod
    def get_by_name_and_email(name: str, email: str):
        try:
            user = User.objects.get(name=name, email=email)
        except User.DoesNotExist:
            user = User(name=name, email=email)
            user.save()
        return user


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

    def comments(self, sort: str = "default"):
        comments = Comment.objects.filter(post=self, parent_comment=None)
        if sort == "old":
            comments = comments.order_by('datetime')
        elif sort == "name":
            comments = comments.order_by('user__name')
        elif sort == "email":
            comments = comments.order_by('user__email')
        else:
            comments = comments.order_by('-datetime')

        return comments

    @property
    def comments_count(self):
        return Comment.objects.filter(post=self).count()

    @staticmethod
    def get_by_id(pk: int):
        return Post.objects.get(pk=pk)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(
        validators=[validate_file_type, validate_file_size],
        upload_to='files/%Y/%m/%d/',
        blank=True,
        null=True,
        default=None
    )
    datetime = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.text

    @property
    def children_comments(self):
        return Comment.objects.filter(parent_comment=self)

    @staticmethod
    def get_by_id(pk: int):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            comment = None
        return comment

    @staticmethod
    def get_by_post(post: Post):
        return Comment.objects.filter(post=post)

    @staticmethod
    def create_by_form(form, post: Post):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        text = form.cleaned_data['text']
        file = form.cleaned_data['file']

        user = User.get_by_name_and_email(name, email)
        comment = Comment(text=text, user=user, post=post, file=file)
        comment.save()
        return comment
