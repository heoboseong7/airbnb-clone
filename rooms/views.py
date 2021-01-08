from math import ceil
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# django가 발생한 request들을 python object로 변환하여 인자로 넘겨줌
# html내에서  변수를 사용하는법 : {{var}}
# logic 사용하는법 ex) for, if :  {%if%} {%else%} {%end if%}  {%for in%} {%end for%}
# 꼭 end를 사용해야함, indent는 하지 않아도 됨
def all_rooms(request):
    page = request.GET.get("page")
    # 해당 변수를 생성할 때 함수가 실행되는 것이 아니라 변수가 사용될 때 함수가 실행됨
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    # page key에 대한 값을 가져옴 없는 경우 기본값 0
    # url에서 오는 것은 get request
    # [offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": rooms,
        },
    )
    # context는 html로 변수를 넘겨줌 context={"template에서의 변수명": 값}