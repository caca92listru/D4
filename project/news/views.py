from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Category,  Comment
from datetime import datetime
from django.shortcuts import redirect

from .filters import PostFilter  # импортируем недавно написанный фильтр
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'News_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

class PostSearch(ListView):
    model = Post
    template_name = 'News_search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 3  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

class PostDetailView(DetailView):
#    model = Post
    template_name = 'details/post_detail.html'
    context_object_name = 'news'
    queryset = Post.objects.all()



class PostCreateView(CreateView):
    template_name = 'details/post_create.html'
    form_class = PostForm
    success_url = '/news/'

# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'details/post_create.html'
    form_class = PostForm
    success_url = '/news_/'
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'details/post_delete.html'
    context_object_name = 'news'
    success_url = '/news/'

class PostEdit(ListView):
    model = Post
    template_name = 'News_edit.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context
