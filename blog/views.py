from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/details.html"
    context_object_name = "post"
