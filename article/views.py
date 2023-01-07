from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, Http404, redirect, reverse
from .models import Article
import random
from django.contrib import messages
from .forms import ArticleForm



def index(request):
    articles = Article.objects.filter(is_deleted__exact=False).order_by('-id')
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
        # print(article.query)
    return render(request, 'article/index.html', {'object_list': articles})


def detail(request, slug=None):
    context = {}
    if slug:
        article = Article.objects.get(slug=slug)
        context['object'] = article  # {"object": article}
        return render(request, 'article/detail.html', context)

    return Http404()


# 1 - uslub
# def create(request):
#     context = {
#
#     }
#     if request.method == "POST":
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         article = Article.objects.create(title=title, content=content)
#         context['object'] = article
#         context['created'] = True
#         #return redirect(reverse('articles:detail', kwargs={"pk": article.id}))
#     return render(request, 'article/create.html', context)

# 2 - uslub
# def __create(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context['object'] = form.data
#             context['created'] = True
#
#     return render(request, 'article/create.html', context)

# 3 - uslub
@login_required
def create(request):
    form = ArticleForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Article created')
        return redirect('articles:list')
    context = {
        'form': form
    }
    return render(request, 'article/create.html', context)


@login_required
def edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=article, files=request.FILES)
        form.save()
        messages.success(request, 'Article Updated')
        return redirect(reverse('articles:detail', kwargs={'slug': article.slug}))
    ctx = {
        'form': form
    }
    return render(request, 'article/edit.html', ctx)

@login_required
def delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        # article.delete()
        article.is_deleted = True
        article.save()
        messages.error(request, f"Article Deleted ({article.id})")
        return redirect('articles:list')
    context = {
        'object': article
    }
    return render(request, 'article/delete.html', context)
