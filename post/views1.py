from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post/post_listado.html'
    context_object_name = 'posts'
    ordering = ['-fecha_publicacion']