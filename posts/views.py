from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from categorias.models import Categoria
from posts.models import Post
from django.db.models import Q, Count, Case, When


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.order_by('-id')
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicacao_comentario=True, then=1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'


class PostDetalhes(UpdateView):
    pass
