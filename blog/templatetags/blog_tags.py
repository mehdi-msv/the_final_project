from django import template
from blog.models import *
from django.utils import timezone
from taggit.models import Tag
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
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:args]

    # Return the dictionary of posts
    return {'posts': posts}


@register.inclusion_tag('blog/blog_tags.html')
def blog_tags():
    """
    This function returns a dictionary of the number of posts in each tag.

    Returns:
        dict: A dictionary where the keys are the tag names and the values
              are the number of posts in each tag.
    """
    # Get all tags
    tags = Tag.objects.all()
    # Create a dictionary to store the number of posts in each tag
    tag_list = []

    # Iterate over each tag and count the number of posts in that tag
    for name in tags:
        tag_list.append(name)

    # Return the dictionary of tag counts
    return {'tags': tag_list}


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
