from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import CForm, CusForm

# Create your views here.


def index(request):
    post = Post.objects.filter(status=1).order_by('-created_on')[:3]
    return render(request, 'index.html', {'post': post})


def blog(request):
    post = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog.html', {'post': post})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment = post.comments.all()

    if request.method == "POST":
        form = CForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.post = post
            com.save()
            messages.success(request, "Comments Added successfully")

        else:
            messages.error(request, "Fill in the required details")

    form = CForm()
    return render(request, "detail.html", {'form': form,
                                           'post': post,
                                           'com': comment,
                                           })


def about(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == "POST":
        c_form = CusForm(request.POST)

        if c_form.is_valid():
            c_form.save()
            messages.success(request, "Thank you for reaching out to me. I'll get back to you soon")

        else:
            messages.warning(request, "please fill in all the required details")

    c_form = CusForm()
    return render(request, 'contact.html', {'form': c_form})
