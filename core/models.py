from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """ Times Stamped Model """

    # 생성된 날짜 수정된 날짜 자동 업데이트
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 데이터베이스에 나타나지 않는 모델 확장을 위해 사용
    class Meta:
        abstract = True