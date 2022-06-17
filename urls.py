from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('qr-code/', qr_code, name='qr_code'),
    path('jpg-to-png/', jpg_to_png, name='jpg_to_png'),
    path('youtube-download/', yt_download, name='yt_download'),
    path('send-comment/', send_comment, name='send_comment'),
    path('link-shorter/', link_shorter, name='link_shorter'),
]
