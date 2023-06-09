from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

import forum.views
import member.views
from mosaicImg.views import mosaic_download

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('forum/', include('forum.urls')), # 테스트용 게시판임
    path('board/', include('board.urls')),
    path('member/', include('member.urls')),
    path('mosaic_download/<int:mos_no>/', mosaic_download, name='mosaic_download'),

]
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)