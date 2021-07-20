from django.shortcuts import render , get_object_or_404
from .models import bloog

def all_blog(request):
    bloogs = bloog.objects.order_by('-date')
    return render(request , 'blog/all_blog.html' , {'bloogs': bloogs})


def detail(request , blog_id):
    blog = get_object_or_404(bloog , pk = blog_id)
    return render(request , 'blog/detail.html' , {'blog': blog})

# Create your views here.
