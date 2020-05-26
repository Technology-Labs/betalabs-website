from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'site/index.html',{} )

def blog_post(request):
    return render (request, 'site/blog_post.html',{} )