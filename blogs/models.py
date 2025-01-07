from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# BlogPost Model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Like Model
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like from {self.user.username} on {self.blog_post.title}"
