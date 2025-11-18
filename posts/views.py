from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm
from django.urls import reverse
# Create your views here.

blog_posts = [
    {
        "id": 1,
        "title": "The Rise of AI in Everyday Life 🤖",
        "content": "Artificial Intelligence is increasingly integrated into our daily routines, from smart assistants to personalized recommendations. This post explores the ethical and practical implications of this rapid technological shift."
    },
    {
        "id": 2,
        "title": "Mastering Python Dictionaries 📖",
        "content": "Dictionaries are one of Python's most versatile data structures. Learn how to create, access, modify, and loop through dictionary items efficiently with practical examples."
    },
    {
        "id": 3,
        "title": "Top 5 Hiking Trails in the Rockies 🏞️",
        "content": "Discover five breathtaking trails in the Rocky Mountains suitable for various skill levels. Essential gear and safety tips are also included to prepare you for your adventure."
    },
    {
        "id": 4,
        "title": "Healthy Eating on a Budget 🥗",
        "content": "Eating well doesn't have to break the bank. This article provides simple strategies and recipes for preparing nutritious, delicious meals while keeping your grocery costs low."
    }
]

def home(request):
    blog_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(blog_posts, 2)
    page_number = request.GET.get("p", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "posts/index.html", {"posts": page_obj})

def post(request, id):
    data = get_object_or_404(Post, id = id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = data
            comment.save()
            posturl = reverse('post', args=[id])
            return HttpResponseRedirect(posturl)

    # try:
    #     data = Post.objects.get(id = id)
    # except Post.DoesNotExist:
    #     raise Http404()

    form = CommentForm()
    
    return render(request, "posts/posts.html", {"post": data, 'form': form})
