from django.db import models
from django.contrib.auth.models import AbstractUser
import News.resourses as rs


class Author(models.Model):
    author = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        #суммарный рейтинг каждой статьи автора умножается на 3
        r1 = Post.objects.filter(author_id=self.pk).values('rating', 'pk')
        # a1 = self.post_set.all().values('rating')
        rate = sum([r1[i]['rating'] for i in range(len(r1))]) * 3
        #суммарный рейтинг всех комментариев автора
        r2 = Comments.objects.filter(author_id=self.author).values('rating')
        rate += sum([r2[i]['rating'] for i in range(len(r2))])
        #суммарный рейтинг всех комментариев к статьям автора
        post_pk = [r1[i]['pk'] for i in range(len(r1))]
        for i in post_pk:
            r3 = Comments.objects.filter(post_id=i).values('rating')
            rate += sum([r3[i]['rating'] for i in range(len(r3))])
        self.rating = rate
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=60, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=rs.TYPES, default=rs.news_type)
    time_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    post = models.TextField()
    rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return f"{self.post[:124:]}..."

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    time_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()