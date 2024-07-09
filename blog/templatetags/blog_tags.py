from django import template
from blog.models import *
from django.utils import timezone
register = template.Library()



@register.inclusion_tag('blog/blog_recent.html')
def blog_latest(args=3):
    """
    This function returns a dictionary of the latest published posts.

    Args:
        args (int): The number of posts to return.

    Returns:
        dict: A dictionary containing the latest published posts.
    """
    # Filter the posts based on status and published date
    posts = Post.objects.filter(
        status='published',
        published_date__lte=timezone.now()
    ).order_by('-pub_date')[:args]

    # Return the dictionary of posts
    return {'posts': posts}



@register.inclusion_tag('blog/blog_cat.html')
def postcategories():
    """
    This function returns a dictionary of the number of posts in each category.

    Returns:
        dict: A dictionary where the keys are the category names and the values
              are the number of posts in each category.
    """
    # Get all published posts
    posts = Post.objects.filter(status='published')

    # Get all categories
    categories = Categories.objects.all()

    # Create a dictionary to store the number of posts in each category
    cat_dict = {}

    # Iterate over each category and count the number of posts in that category
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    # Return the dictionary of category counts
    return {'categories': cat_dict}



@register.inclusion_tag('website/latest_posts.html')
def latest_posts(args=6):
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
        published_date__lte=timezone.now()
    ).order_by('-pub_date')[:args]

    # Return the dictionary of posts
    return {'posts': posts}



@register.simple_tag(name='comments_count')
def get_comments_count(post_id):
    """
    This function returns the count of approved comments for a given post.

    Args:
        post_id (int): The ID of the post.

    Returns:
        int: The count of approved comments for the post.
    """
    # Filter comments based on post ID and approved status
    comments = Comment.objects.filter(post_id=post_id, approved=True)

    # Return the count of comments
    return comments.count()
