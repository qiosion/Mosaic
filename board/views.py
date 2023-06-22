import os
import traceback

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path

import member
from board.models import Board
from mosaicImg.models import MosaicImg
from mosaicImg.views import get_mosaic_haar
from mosaicImg.views import get_shuffle_img
from mosaicImg.views import get_face_shuffle
from mosaicImg.views import get_mosaic_zoom
from mosaicImg.views import land_mosaic
from config import settings


# 게시글 작성 함수
@login_required(login_url='/member/login')
def create(request):
    if request.method == "POST":
        board_title = request.POST.get('board_title')
        board_content = request.POST.get('board_content')
        mos_up = request.FILES.get('mos_up')
        selected_type = request.POST.get('type')
        print('selected_type : ', selected_type)

        # 제목과 업로드 파일만 요구함
        if board_title and mos_up:
            member = request.user
            board = Board(member=member, board_title=board_title, board_content=board_content)
            board.save()

            board_no = board.board_no
            board_instance = get_object_or_404(Board, board_no=board_no)
            mos = MosaicImg(mos_up=mos_up, board_no=board_instance)
            mos.save()

            # 모자이크 처리
            if selected_type == 'harr':
                get_mosaic_haar(request, mos.mos_no)
            elif selected_type == 'test':
                get_mosaic_zoom(request, mos.mos_no)
            elif selected_type == 'jia':
                land_mosaic(request, mos.mos_no)
            elif selected_type == 'shuffle':
                get_shuffle_img(request, mos.mos_no)
            elif selected_type == 'faceShuffle':
                get_face_shuffle(request, mos.mos_no)
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

# 게시글 조회 함수
def read(request, board_no):
    board = Board.objects.get(board_no=board_no)
    board_instance = get_object_or_404(Board, board_no=board_no)
    mos = MosaicImg.objects.get(board_no=board_instance)

    context = { 'board': board, 'mos': mos }

    return render(
        request,
        'board/read.html',
        context
    )

# 글 목록
def list(request):
    board = Board.objects.all().order_by('-board_date')

    # 페이지네이션
    page = request.GET.get('page')
    paginator = Paginator(board, 10)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger: # page 입력하지 않았을 경우 예외처리
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage: # page값이 너무 클 경우(존재하지 않는 경우) 예외처리
        page = paginator.num_pages # 가장 마지막 페이지
        page_obj = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    context = { 'board': board,
                'page_obj': page_obj,
                'paginator': paginator,
                'custom_range': custom_range }

    return render(
        request,
        'board/list.html',
        context
    )

# 작성글 확인
def my_list(request):
    member = request.user
    board = Board.objects.filter(member=member).order_by('-board_date')

    # 페이지네이션
    page = request.GET.get('page')
    paginator = Paginator(board, 10)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger: # page 입력하지 않았을 경우 예외처리
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage: # page값이 너무 클 경우(존재하지 않는 경우) 예외처리
        page = paginator.num_pages # 가장 마지막 페이지
        page_obj = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    context = { 'board': board,
                'page_obj': page_obj,
                'paginator': paginator,
                'custom_range': custom_range }

    return render(
        request,
        'board/my_list.html',
        context
    )

# 게시글 수정
def update(request, board_no):
    board = get_object_or_404(Board, board_no=board_no)
    mos = get_object_or_404(MosaicImg, board_no=board)

    if request.method == 'POST':
        board_title = request.POST.get('board_title')
        board_content = request.POST.get('board_content')
        mos_up = request.FILES.get('mos_up')
        selected_type = request.POST.get('type')
        try:
            if board_title:
                board.board_title = board_title
                board.board_content = board_content
            board.save()

            if mos_up is None:
                # 아무 파일도 선택하지 않은 경우 기존 파일 사용
                mos_up = mos.mos_up

            mos.mos_up = mos_up
            mos.save()
            if mos_up:
                if selected_type == 'harr':
                    get_mosaic_haar(request, mos.mos_no)
                elif selected_type == 'shuffle':
                    get_shuffle_img(request, mos.mos_no)
                elif selected_type == 'faceShuffle':
                    get_face_shuffle(request, mos.mos_no)

            return redirect('read', board_no=board.board_no)

        except Exception as e:
            error_message = '게시글 업데이트에 실패했습니다.'
            return render(request,
                          'board/update.html',
                          {'board': board, 'mos': mos,
                           'error_message': error_message})
    elif request.method == 'GET':
        context = {'board': board, 'mos': mos}
        return render(
            request,
            'board/update.html',
            context
        )

# 게시글 삭제
def delete(request, board_no):
    login_session = request.session.get('login_session', '')
    board = get_object_or_404(Board, board_no=board_no)

    # 게시글 작성자와 세션의 아이디가 동일한 경우에만 삭제 가능
    if login_session == board.member:
        try:
            board.delete()

        except Exception as e:
            error_message = '게시글 삭제에 실패했습니다.'
            return render(request,
                          'board/read.html',
                          {'board': board,
                           'error_message': error_message})
        return redirect('list')
    else:
        error_message = '게시글 작성자가 아닙니다'
        return render(request,
                      'board/read.html',
                      {'board': board, 'error_message': error_message})
