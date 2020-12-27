from django.db import models

# Create your models here.


class TimeStampedModel(model.Model):
    """ Times Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # 데이터베이스에 나타나지 않는 모델 확장을 위해 사용
    class Meta:
        abstract = True