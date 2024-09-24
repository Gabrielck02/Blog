from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']  # Campos que se pueden editar
    template_name = 'post/post_form.html'  # La plantilla del formulario
    success_url = reverse_lazy('post:post_listado')  # Redirigir tras editar

    # Verifica si el usuario es el autor de la publicación
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor