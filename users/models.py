from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """ Custom User Modes """

    # 데이터베이스에 bio column이 새로 생성되었을 때 기존의 row에 default값이 추가되어 들어감
    # default를 사용하거나 NULL 값을 활성화 null=true
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        # (DB로 보내질 값, form에 보여질 값)
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CYURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )
    # null은 DB의 허용 / blank는 form에서 공백을 허용하게 해줌
    avatar = models.ImageField(null=True, blank=True)
    # max_length 설정 필수 choices는 form에만 영향, DB에는 영향 없음
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CYURRENCY_CHOICES, max_length=3, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)
