from django.urls import path
from .views import PostCreateView
from .views1 import PostListView
from .views2 import PostDetailView
from .views3 import PostDeleteView
from .views4 import PostUpdateView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='post_listado'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detalles'),
    path('post/nuevo/', PostCreateView.as_view(), name='post_crear'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_eliminar'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post_editar'),
]