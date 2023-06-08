import os

from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path

import member
from board.models import Board
from config import settings


@login_required(login_url='/member/login')
def create(request):
    if request.method == "POST":
        board_title = request.POST.get('board_title')
        board_content = request.POST.get('board_content')
        board_upload = request.FILES.get('board_upload')
        print('board_title : ', board_title)
        print('board_content : ', board_content)
        print('board_upload : ', board_upload)

        if board_title and board_upload:
            member = request.user
            board = Board(member=member, board_title=board_title, board_content=board_content, board_upload=board_upload)
            board.save()
            return redirect('list')
            # return redirect('read', board_no=board.board_no)
        else:
            error_message = '제목 작성과 업로드할 파일을 첨부를 확인하세요'
            return render(
                request,
                'board/create.html',
                {'error_message': error_message}
            )
    elif request.method == "GET":
        return render(
            request,
            'board/create.html'
        )

def mosaic_download(request, board_no):
    # mosaic_path = f"media/mosaic/{board_no}.jpg"
    mosaic_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{board_no}.png')
    mosaic_url = settings.MEDIA_URL + 'mosaic/' + f'mosaic_{board_no}.png'

    board = Board.objects.get(board_no=board_no)
    board.board_download = mosaic_path
    board.save()

    return redirect(mosaic_url)

# urlpatterns = [
#     path('board/<int:board_id>/mosaic_download/', mosaic_download, name='mosaic_download'),
# ]

# def read(request, board_no):
#     post = Board.objects.get(board_no=board_no)
#     context = { 'post': post }
#
#     return render(
#         request,
#         'board/read.html',
#         context
#     )

def list(request):
    posts = Board.objects.all().order_by('-board_date')
    context = { 'posts': posts }

    return render(
        request,
        'board/list.html',
        context
    )