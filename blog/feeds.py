from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Cia Blog News"
    link = "/sitenews/"
    description = "Cia cafe all posts from blog"

    def items(self):
        return Post.objects.filter(status = 'published' )

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content