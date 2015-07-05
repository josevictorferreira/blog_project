from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='media/post_images', default='media/post_images/default.img')

    def __unicode__(self):
        return self.title