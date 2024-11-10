from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic import ListView, DetailView, FormView

from .forms import PostForm
from .models import Post

def indexFBV(request):
    latest_posts_list = Post.objects.order_by("-published_date")
    template = loader.get_template("posts/index.html")
    context = {
        "latest_posts_list": latest_posts_list,
        "sub_domen": "fbv"
    }
    return render(request, "posts/index.html", context)

def detailFBV(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        "post": post,
        "sub_domen": "fbv"
    }
    return render(request, "posts/detail.html", context)

class IndexCBV(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "latest_posts_list"
    ordering = ["-published_date"]

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context["sub_domen"] = "cbv" 
        return context 

class DetailCBV(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['sub_domen'] = 'cbv' 
        return context 
    
class PostCreateCBV(FormView):
    template_name = "posts/create_post.html"
    form_class = PostForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)