from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post/post_eliminar.html'  # Plantilla para confirmar eliminación
    success_url = reverse_lazy('post:post_listado')  # Redirigir tras eliminar

    # Verifica si el usuario es el autor de la publicación
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor