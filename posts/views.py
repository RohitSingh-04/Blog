from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    html = ""
    for post in blog_posts:
        html += f'''
            <div>
            <a href = '{post['id']}'> {post['title']}</h1>
            </div>
'''
    return HttpResponse(html)

def post(request, id):
    data = None

    for posts in blog_posts:
        if posts['id'] == id:
            data = posts
            break 

    if not data:
        return HttpResponseNotFound("<h1 style='color:red;'> Not found</h1>")
    
    return HttpResponse(f'<h1>{data["title"]}</h1><p>{data["content"]}</p>')

def google(request, id):
    url = reverse('post', args=[id])
    return HttpResponseRedirect(url)