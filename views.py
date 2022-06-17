import os

import pyshorteners

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from project import settings
import qrcode
from PIL import Image

from .forms import QRcodeForm, JpgToPngForm, YouTubeDownloadForm, LinkShortenerForm
from pytube import YouTube


# Main page

def index(request):
    # deleting all files from media directory as user goes to home page because the files will
    while True:
        directory = 'media/'
        for file in os.listdir(directory):
            os.remove(os.path.join(directory, file))
        return render(request, 'reformation/index.html')


# QR codes section

def qr_code(request):
    # displaying form
    qr_code_form = QRcodeForm

    context = {
        'qr_code_form': qr_code_form,
    }

    # working with data from form done by user

    if request.method == 'POST':
        form = QRcodeForm(data=request.POST)
        if form.is_valid():
            form.save()

        data = request.POST

        name = data['name']
        link = data['link']

        # dimension - gives users possibility to choose a quality and dimension for their qr code
        dimension = data['dimension']

        qr_code_name = f'{name}.png'

        qr_code_link = qrcode.make(link)

        # store a qr code done by user in a media_root to get a chance to display it in html.
        qr_code_link.save(settings.MEDIA_ROOT / qr_code_name)

        context = {
            'img': qr_code_name,
            'dimension': dimension,

        }

        return render(request, "reformation/components/_qr_codes_detail.html", context)

    return render(request, 'reformation/qr_code.html', context)


# jpg to png section

def jpg_to_png(request):
    jpg_to_png_form = JpgToPngForm

    context = {
        'jpg_to_png_form': jpg_to_png_form,
    }

    if request.method == 'POST':
        form = JpgToPngForm(request.POST, request.FILES)

        # handling the data received
        data_name = request.POST
        files_data = request.FILES

        # save if is valid
        if form.is_valid():
            # extracting file received from all data
            files = files_data['images']

            # extracting name for png from user that is received from all data
            name = data_name['name']

            # open jpg file
            image = Image.open(files)

            # make it png and save
            image.save(settings.MEDIA_ROOT / f'{name}.png', 'png')

            context = {
                'reformed_data': f'{name}.png'
            }

            return render(request, "reformation/components/_reformed_data_detail.html", context)

    return render(request, 'reformation/jpg_to_png.html', context)


# YouTube download section

def yt_download(request):
    yt_download_form = YouTubeDownloadForm

    context = {
        'yt_download_form': yt_download_form,
    }

    if request.method == 'POST':
        form = YouTubeDownloadForm(data=request.POST)
        if form.is_valid():
            form.save()

        # handling data received
        data = request.POST

        # extracting only link from data received
        link = data['link']

        # check and make sure that link is from YouTube
        check_link = link.startswith('https://youtu.be/')

        if check_link:
            yt_obj = YouTube(link)

            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

            filters.get_highest_resolution().download('media/', filename='video.mp4')

            return render(request, "reformation/components/_yt_downloaded_detail.html")

    return render(request, 'reformation/yt_download.html', context)


# link shortener section

def link_shorter(request):
    link_shorter_form = LinkShortenerForm

    context = {
        'link_shorter_form': link_shorter_form,
    }

    if request.method == 'POST':
        data = request.POST

        link = data['link']

        shortener = pyshorteners.Shortener()

        check_link = link.startswith("https://")
        if check_link:
            result = shortener.tinyurl.short(link)

            context = {
                'result': result
            }
            return render(request, 'reformation/link_shortener.html', context)

    return render(request, 'reformation/link_shortener.html', context)


# send comment section

def send_comment(request):
    if request.method == 'POST':
        data = request.POST

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        subject = data['subject']
        comment = data['comment']

        send_mail(
            f'{subject}',
            first_name + ' ' + last_name + f'\n\n{comment}' + f'\n\n\n{email}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]
        )
        return redirect('index')

    return render(request, 'reformation/send_email.html')
