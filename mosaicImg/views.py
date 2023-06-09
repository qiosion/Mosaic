import os

from django.shortcuts import render, redirect

from config import settings
from mosaicImg.models import MosaicImg


def mosaic_download(request, mos_no):
    # mosaic_path = f"media/mosaic/{board_no}.jpg"
    mos = MosaicImg.objects.get(mos_no=mos_no)
    # board_no = mos.board_no
    board_no = str(mos.board_no.board_no).zfill(8)
    print('여기 : ', board_no)
    mosaic_path = os.path.join(settings.MEDIA_ROOT, 'mosaic', f'mosaic_{board_no}.jpg')
    print('mosaic_path 는 ' , mosaic_path)
    mosaic_url = settings.MEDIA_URL + 'mosaic/' + f'mosaic_{board_no}.jpg'
    print('mosaic_url 는 ' , mosaic_url)

    mos.mos_down = mosaic_path
    mos.save()

    return redirect(mosaic_url)