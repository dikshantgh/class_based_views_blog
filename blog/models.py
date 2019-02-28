from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='p')


class Post(models.Model):

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='d')

    # objects = models.Manager() # The default manager. for example Post.objects.all()
    # Our custom manager. for example Post.published.all()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:detail_posts', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(
        Post, related_name="comments", on_delete="CASCADE")
    name = models.CharField(max_length=250)
    comment = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "Comment by "+str(self.name)+"on the post"+str(self.post)
