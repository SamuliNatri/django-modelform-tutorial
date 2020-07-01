from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, PostDeleteForm
from blog.models import Post


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_create')
    else:
        form = PostForm()
    return render(request,
                  'blog/post_create.html',
                  {
                      'form': form
                  })


def post_edit(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,
                        instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_create')
    else:
        form = PostForm(instance=post)

    return render(request,
                  'blog/post_edit.html',
                  {
                      'form': form,
                      'post': post
                  })
    

def post_delete(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostDeleteForm(request.POST,
                              instance=post)
        if form.is_valid():
            post.delete()
            return redirect('post_create')
    else:
        form = PostDeleteForm(instance=post)

    return render(request, 'blog/post_delete.html',
                  {
                      'form': form,
                      'post': post,
                  })