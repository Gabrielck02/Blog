from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detalles.html'
    context_object_name = 'post'