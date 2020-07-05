from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
                blank=True,
                processors=[#<- 어떤 가공할지
                    Thumbnail(300,300),    
                ],
                format='JPEG', # 이미지 포멧(jpg or png)
                options={ #이미지 포멧 관련 옵션
                    'quality': 90,
                }
    )
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m)       
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

