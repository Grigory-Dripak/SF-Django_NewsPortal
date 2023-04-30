article_type = 'A'
news_type = 'N'

TYPES = [(article_type, 'article'), (news_type, 'news')]


class Rating:
    rating = 0

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
