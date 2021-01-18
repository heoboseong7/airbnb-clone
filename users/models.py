import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail

# Create your models here.


class User(AbstractUser):
    """ Custom User Modes """

    # 데이터베이스에 bio column이 새로 생성되었을 때 기존의 row에 default값이 추가되어 들어감
    # default를 사용하거나 NULL 값을 활성화
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
    avatar = models.ImageField(upload_to="avatars", blank=True)
    # max_length 설정 필수 choices는 form에만 영향, DB에는 영향 없음
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        choices=CYURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify Airbnb Account",
                f"Verify account, this is your code:{secret}",
                setting.EMAIL_FROM,
                [self.email],
                fail_silently=False,
            )
        return
