from django.shortcuts import render, HttpResponse
from post.models import Post
# Create your views here.


def home(request):
    allPosts = Post.objects.all()
    context = {"posts": allPosts}
    return render(request, 'home.html', context)


def post(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        url = request.POST.get('url')
        desc = request.POST.get('desc')
        ins = Post(caption=caption, url=url, desc=desc)
        ins.save()
    return render(request, 'post.html')
