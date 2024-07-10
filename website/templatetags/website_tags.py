from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()


@register.inclusion_tag('website/latest_posts.html')
def latest_posts(args=3):
    """
    This function returns a dictionary of the latest published posts.

    Args:
        args (int): The number of posts to return.

    Returns:
        dict: A dictionary containing the latest published posts.
    """
    # Filter the posts based on status, published date, and order them by published date in descending order
    posts = Post.objects.filter(
        status='published',
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:args]

    # Return the dictionary of posts
    return {'posts': posts}