from django.db import models
from HTMLParser import HTMLParser
import re

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post_images', default='post_images/default.img')

    def __unicode__(self):
        return self.title

    def text_to_html(self):
        splitText = list([x for x in re.split(r'\n', self.text) if not x in ['', '\r']])
        newText = ""
        for i in range(len(splitText)):
            splitText[i] = '<p>' + splitText[i] + '</p>'
            newText += splitText[i]
        htmlparser = HTMLParser() #Cria o objeto HTMLParser, para converter o texto para HTML
        newText = htmlparser.unescape(newText)
        return newText