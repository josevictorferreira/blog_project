from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage, InvalidPage
from models import Post, Tag

# Create your views here.
def home(request):
    post_list = Post.objects.all()[::-1]
    paginator = Paginator(post_list, 2)
    tags = Tag.objects.all()[::-1]

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
        actual = int(page)
    except (PageNotAnInteger, InvalidPage):
        posts = paginator.page(1)
        actual = 1
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        actual = int(paginator.num_pages)

    list_pages_template = get_num_pages(actual, paginator.num_pages)

    return render_to_response('home.html', {'posts':posts, 'pages': list_pages_template, 'tags':tags})

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tags = Tag.objects.all()[::-1]

    return render_to_response('post.html', {'post':post, 'tags':tags})

def view_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    post_list = Post.objects.filter(tag=tag)[::-1]
    paginator = Paginator(post_list, 2)
    tags = Tag.objects.all()[::-1]

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
        actual = int(page)
    except (PageNotAnInteger, InvalidPage):
        posts = paginator.page(1)
        actual = 1
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        actual = int(paginator.num_pages)

    list_pages_template = get_num_pages(actual, paginator.num_pages)

    return render_to_response('home.html', {'posts':posts, 'pages': list_pages_template, 'tags':tags})

def get_num_pages(actual, max):
    def put_dots(pages):
        newPages = []
        for i in range(len(pages)-1):
            if pages[i+1] - pages[i] > 1:
                newPages.append(pages[i])
                newPages.append(0)
            else:
                newPages.append(pages[i])
        newPages.append(pages[len(pages)-1])
        return newPages

    suc = lambda n: n + 1
    ant = lambda n: n - 1
    pages = []
    left = actual - 1
    right = max - actual
    pages.append(actual)
    if right > 3:
        pages.append(suc(actual))
        pages.append(suc(suc(actual)))
        pages.append(max)
    else:
        for i in range(actual, max+1):
            if i != actual:
                pages.append(i)
    if left > 3:
        pages.append(ant(actual))
        pages.append(ant(ant(actual)))
        pages.append(1)
    else:
        for i in range(1, actual):
            if i != actual:
                pages.append(i)
    return put_dots(sorted(pages))
    
