from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from forum.forms import PostForm
from forum.models import Post


# 게시판 글 생성
@login_required(login_url='/member_test/login')
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
            post.member = request.user
            post.save()
        return redirect('/forum/read/' + str(post.id))


def list(request):
    posts = Post.objects.all().order_by('-create_date')
    context = { 'posts': posts }

    return render(
        request,
        'forum/list.html',
        context
    )

def read(request, forum_id):
    post = Post.objects.get(id=forum_id)
    context = { 'post': post }

    return render(
        request,
        'forum/read.html',
        context
    )

@login_required(login_url='/member_test/login')
def delete(request, forum_id):
    post = Post.objects.get(id=forum_id)
    if request.user != post.member:
        return redirect('/forum/read/' + str(forum_id))
    post.delete()
    return redirect('/forum/list')

@login_required(login_url='/member_test/login')
def update(request, forum_id):
    post = Post.objects.get(id=forum_id)

    if request.user != post.member:
        return redirect('/forum/read/' + str(forum_id))

    if request.method == "GET":
        postForm = PostForm(instance=post)
        context = { 'postForm': postForm }
        return render(
            request,
            "forum/update.html",
            context
        )
    elif request.method == "POST":
        postForm = PostForm(request.POST, instance=post)

        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/forum/read/' + str(post.id))
