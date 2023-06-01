from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import member
from board.models import Board

# @login_required(login_url='/member/login')
def create(request):
    if request.method == "POST":
        board_title = request.POST.get('board_title')
        board_content = request.POST.get('board_content')
        board_upload = request.FILES.get('board_upload')

        if board_title and board_upload:
            member = request.user
            board = Board(member=member, board_title=board_title, board_content=board_content, board_upload=board_upload)
            board.save()

            return redirect('read', board_no=board.board_no)
        else:
            error_message = '제목 작성과 업로드할 파일을 첨부를 확인하세요'
            return render(
                request,
                'board/create.html',
                {'error_message': error_message}
            )
    else:
        return render(
            request,
            'board/create.html'
        )

def read(request, board_no):
    post = Board.objects.get(board_no=board_no)
    context = { 'post': post }

    return render(
        request,
        'board/read.html',
        context
    )

def list(request):
    posts = Board.objects.all().order_by('-board_date')
    context = { 'posts': posts }

    return render(
        request,
        'board/list.html',
        context
    )