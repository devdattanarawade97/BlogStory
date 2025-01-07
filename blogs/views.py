from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Category, Like
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Landing Page - Display Blog List
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
def blog_list(request):
    # Get all published blogs
    blogs = BlogPost.objects.filter(is_published=True).order_by('-publish_date')
    
    # Filter by date if requested
    filter_date = request.GET.get('date')
    if filter_date:
        try:
            filter_date = timezone.datetime.strptime(filter_date, '%Y-%m-%d').date()
            blogs = blogs.filter(publish_date__date=filter_date)
        except ValueError:
            pass  # Handle invalid date format gracefully
    
    # Filter by category if selected
    filter_category = request.GET.get('category')
    if filter_category:
        blogs = blogs.filter(category_id=filter_category)

    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
        'filter_date': filter_date,
    }
    return render(request, 'index.html', context)



# Blog Detail - View Full Blog Post
@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'blog_detail.html', context)

# Filter Blogs by Category
def filter_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    blogs = BlogPost.objects.filter(category=category, is_published=True)
    context = {
        'blogs': blogs,
        'category': category,
    }
    return render(request, 'blogs/index.html', context)

# Like Blog Post
def like_blog(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.user.is_authenticated:
        if Like.objects.filter(user=request.user, blog_post=blog).exists():
            # User has already liked the post
            messages.info(request, 'You have already liked this blog.')
        else:
            # Create a new Like
            Like.objects.create(user=request.user, blog_post=blog)
            blog.like_count += 1
            blog.save()
            messages.success(request, 'You liked this blog.')
    else:
        messages.error(request, 'You need to log in to like a blog.')

    return redirect('blog_detail', pk=pk)

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user and log them in
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('blog_list')  # Redirect to the blog list or home page
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    # Render the login page with the form
    return render(request, 'login.html', {'form': form})
