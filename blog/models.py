from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=250, null= False, blank = False)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    intro = models.TextField(blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length = 20)
    image = models.ImageField(upload_to= 'pics')
    slug = models.SlugField(blank= True, unique= True)

    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    

class Email(models.Model):
    email = models.EmailField()

