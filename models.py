from django.db import models


class QRcode(models.Model):
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    link = models.CharField(max_length=150)
    dimension = models.IntegerField(blank=True, default=500)

    def __str__(self):
        return self.username


class JpgToPng(models.Model):
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=55, null=False, default='')
    images = models.ImageField(blank=False)

    def __str__(self):
        return self.username


class YouTubeDownload(models.Model):
    username = models.CharField(max_length=25)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.username
