from django.db import models

# Create your models here.
from members.models import User


class Post(models.Model):
    """
    인스타그램 포스트
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    # 포스트 한개는 여러개의 사용자 like를 가질 수 있다. 마찬가지로 사용자 like는 여러개의 post에 있을 수 있다.
    like_users = models.ManyToManyField(User, related_name='like_post_set', through='PostLike')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} | {self.created}'


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images')


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)


class PostLike(models.Model):
    """
    사용자가 좋아요 누른 Post정보를 저장
    Many-To-Many 필드를 중간 모델을 거쳐 사용
    언제 생성 되었는지를 Extra field로 저장
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
