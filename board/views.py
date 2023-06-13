import os
import traceback

from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path

import member
from board.models import Board
from mosaicImg.models import MosaicImg
from mosaicImg.views import get_mosaic_haar
from config import settings


@login_required(login_url='/member/login')
def create(request):
    if request.method == "POST":
        board_title = request.POST.get('board_title')
        board_content = request.POST.get('board_content')
        mos_up = request.FILES.get('mos_up')
        print('board_title : ', board_title)
        print('board_content : ', board_content)
        print('mos_up : ', mos_up)

        if board_title and mos_up:
            member = request.user
            board = Board(member=member, board_title=board_title, board_content=board_content)
            board.save()
            board_no = board.board_no
            print('board_no : ', board_no)
            # mos = MosaicImg(mos_up=mos_up, board_no=board_no)
            board_instance = get_object_or_404(Board, board_no=board_no)
            mos = MosaicImg(mos_up=mos_up, board_no=board_instance)
            mos.save()
            get_mosaic_haar(request, mos.mos_no)
            # return redirect('list')
            return redirect('read', board_no=board.board_no)
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


# urlpatterns = [
#     path('board/<int:board_id>/mosaic_download/', mosaic_download, name='mosaic_download'),
# ]

def read(request, board_no):
    board = Board.objects.get(board_no=board_no)
    board_instance = get_object_or_404(Board, board_no=board_no)
    mos = MosaicImg.objects.get(board_no=board_instance)
    print("read 하면 mos_up : ", mos.mos_up)
    print("read 하면 mos_down : ", mos.mos_down)
    context = { 'board': board, 'mos': mos }

    return render(
        request,
        'board/read.html',
        context
    )

def list(request):
    board = Board.objects.all().order_by('-board_date')
    context = { 'board': board }

    return render(
        request,
        'board/list.html',
        context
    )

def update(request, board_no):
    board = get_object_or_404(Board, board_no=board_no)
    mos = get_object_or_404(MosaicImg, board_no=board)
    if request.method == 'POST':
        try:
            board_title = request.POST.get('board_title')
            board_content = request.POST.get('board_content')
            mos_up = request.FILES.get('mos_up')
            print('board_title : ', board_title)
            print('board_content : ', board_content)
            print('mos_up : ', mos_up)

            if board_title and mos_up:
                board.board_title = board_title
                board.board_content = board_content
                board.save()
                mos.mos_up = mos_up
                mos.save()
                return redirect('read', board_no=board.board_no)

        except Exception as e:
            error_message = '게시글 업데이트에 실패했습니다.'
            return render(request,
                          'board/update.html',
                          {'board': board, 'mos': mos,
                           'error_message': error_message})
    context = {'board': board, 'mos': mos}

    return render(
        request,
        'board/update.html',
        context
    )
