# templatetags 폴더명만 허용
from django import template

register = template.Library()

# ()을 붙이지 않으면 load를 한 후에 사용가능
# 함수명과 필터 이름이 같은 경우 name 설정을 해주지 않아도 됨
@register.filter
def sexy_capitals(value):
    return value.capitalize()
