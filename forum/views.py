from django.shortcuts import render, redirect

from forum.forms import PostForm
from forum.models import Post


# 게시판 글 생성
def create(request):
    if request.method == "GET":
        postForm = PostForm()
        context = { 'postForm': postForm }
        return render(
            request,
            "forum/create.html",
            context
        )
    elif request.method == "POST":
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect("/admin/")


def list(request):
    posts = Post.objects.all().order_by('-create_date')
    context = { 'posts': posts }

    return render(
        request,
        'forum/list.html',
        context
    )

def read(request):
    post = Post.objects.get(id=1)
    context = { 'post': post }

    return render(
        request,
        'forum/read.html',
        context
    )