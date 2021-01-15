from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # clean_으로 시작해야 함
    # cleaned_data 는 clean_ 함수들의 리턴값의 모음
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username="email")
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        print("clean password")