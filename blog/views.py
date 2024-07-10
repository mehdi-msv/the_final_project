from django.shortcuts import render, get_object_or_404, redirect
from blog.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.utils import timezone
from blog.forms import CommentForm
import sweetify
# Create your views here.


def blog_view(request, **kwargs):
    """
    View function for rendering the blog page.
    It retrieves posts based on the provided kwargs and paginates them.
    
    Args:
        request (HttpRequest): The HTTP request object.
        **kwargs: Additional keyword arguments for filtering the posts.
        
    Returns:
        HttpResponse: The rendered blog page with the posts.
    """
    
    # Retrieve published posts
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        status='published'
    ).order_by('-pub_date')
    
    # Filter posts based on the provided kwargs
    if kwargs.get('author_user'):
        posts = posts.filter(author__username=kwargs['author_user'])
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name=kwargs['tag_name'])
    
    # Paginate the posts
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)

    # Create the context dictionary
    context = {'posts': posts}
    
    # Render the blog page with the posts
    return render(request, 'blog/blog.html', context)


def blog_single(request, pid):
    """
    This function displays a single blog post and handles form submission for comments.
    
    Args:
        request: The HTTP request object.
        pid: The primary key of the blog post.
        
    Returns:
        Rendered HTML page displaying the single blog post.
    """
    
    # Get the specified blog post
    post = get_object_or_404(Post, pk=pid, status='published', pub_date__lte=timezone.now())
    
    # Check if the post requires login
    if post.login_required and not request.user.is_authenticated:
        # Require login for specific posts
        return redirect('account_login')  # Redirect to login page
    
    # Get the next and previous posts
    next_post = Post.objects.filter(pub_date__gt=post.pub_date, status='published').order_by('pub_date').first()
    prev_post = Post.objects.filter(pub_date__lt=post.pub_date, status='published').order_by('-pub_date').first()
    
    # Increment the number of views for the post
    post.counted_views += 1
    post.save()
    
    if request.method == 'POST':
        # Handle form submission for comments
        form = request.POST.copy()
        form['post'] = post.id
        form = CommentForm(form)
        
        if form.is_valid():
            # Save the comment
            form.save()
            sweetify.success(request, 'Your comment submitted successfully')
        else:
            sweetify.error(request, 'Your comment didn\'t submit')
    
    # Display form for comments
    form = CommentForm()
    comments = Comment.objects.filter(post__id=pid, approved=True)
    
    # Render the HTML page
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'next_post': next_post,
        'prev_post': prev_post
    }
    
    return render(request, 'blog/blog-details.html', context)


def blog_category(request, cat_name):
    """
    This function displays a list of blog posts based on the provided category name.

    Args:
        request: The HTTP request object.
        cat_name: The name of the category.

    Returns:
        Rendered HTML page displaying the filtered blog posts.
    """
    # Filter blog posts based on status and category name
    posts = Post.objects.filter(status='published')
    posts = posts.filter(category__name=cat_name)
    
    # Create context dictionary with the filtered posts
    context = {
        'posts': posts,
    }
    
    # Render the HTML page with the context
    return render(request,'blog/blog.html', context)


def blog_search(request):
    """
    This function displays a list of blog posts based on the search query.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page displaying the filtered blog posts.
    """
    # Retrieve all published posts
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        status='published'
    ).order_by('-pub_date')

    # If the request method is GET and a search query is provided, filter the posts
    if request.method == 'GET':
        # Retrieve the search query from the request
        search_query = request.GET.get('s')
        if search_query:
            posts = posts.filter(content__contains=search_query)

    # Create a context dictionary with the filtered posts
    context = {'posts': posts}

    # Render the HTML page with the context
    return render(request, 'blog/blog.html', context)