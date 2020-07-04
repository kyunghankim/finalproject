# from django.db import models
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings



class Profile(models.Model):
    nickname = models.CharField(max_length=20, blank=True)
    image = ProcessedImageField(
                        blank=True,
                        upload_to='profile/image/', #<-img파일들 어디에 저장할지 지정
                        processors=[Thumbnail(300,300)], format='png',
                        )
    # on_delete: 유저 삭제시 프로필은 어떻게 할지
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # status = models.TextField(max_length=50, blank=True)
    #<- 1대1로 연결(1명의유저,1개의profile)

        

