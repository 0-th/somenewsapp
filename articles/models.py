from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='article_detail', args=[str(self.pk)])


class Comment(models.Model):
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.CharField(max_length=1000)
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse(viewname='article_detail', args=[str(self.pk)])
