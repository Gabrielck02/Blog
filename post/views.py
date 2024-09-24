from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('blog:post_listado')  

    def form_valid(self, form):
        form.instance.autor = self.request.user  
        return super().form_valid(form)

