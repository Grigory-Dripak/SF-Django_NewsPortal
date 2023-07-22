from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache

import News.resourses as rs
from django.db.models import Sum


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        rate = 0
        r1 = self.posts.aggregate(postRating=Sum('rating'))
        rate += r1.get('postRating') * 3
        r2 = self.author.comments.aggregate(commentRating=Sum('rating'))
        rate += r2.get('commentRating')
        for i in self.posts.all():
            r3 = i.comments_set.aggregate(postcommentRating=Sum('rating'))
            rate += r3.get('postcommentRating')
        # #суммарный рейтинг каждой статьи автора умножается на 3
        # if Post.objects.filter(author_id=self.pk).exists():
        #     r1 = Post.objects.filter(author_id=self.pk).values('rating', 'pk')
        #     rate += sum([r1[i]['rating'] for i in range(len(r1))]) * 3
        #     #суммарный рейтинг всех комментариев к статьям автора
        #     post_pk = [r1[i]['pk'] for i in range(len(r1))]
        #     for i in post_pk:
        #         r3 = Comments.objects.filter(post_id=i).values('rating')
        #         rate += sum([r3[i]['rating'] for i in range(len(r3))])
        # #суммарный рейтинг всех комментариев автора
        # if Comments.objects.filter(author_id=self.author).exists():
        #     r2 = Comments.objects.filter(author_id=self.author).values('rating')
        #     rate += sum([r2[i]['rating'] for i in range(len(r2))])
        self.rating = rate
        self.save()

    def __str__(self):
        return f'{self.author}'


class Category(models.Model):
    category = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.category}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    type = models.CharField(max_length=1, choices=rs.TYPES, default=rs.news_type)
    time_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post = models.TextField()
    rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    def preview(self):
        return f"{self.post[:124:]}..."

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.title}: {self.author}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    time_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
