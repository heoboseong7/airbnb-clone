from math import ceil
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

# django가 발생한 request들을 python object로 변환하여 인자로 넘겨줌
# html내에서  변수를 사용하는법 : {{var}}
# logic 사용하는법 ex) for, if :  {%if%} {%else%} {%end if%}  {%for in%} {%end for%}
# 꼭 end를 사용해야함, indent는 하지 않아도 됨
def all_rooms(request):
    page = request.GET.get("page", 1)
    # paginator가 자동으로 default 값을 처리해줌
    # 해당 변수를 생성할 때 함수가 실행되는 것이 아니라 변수가 사용될 때 함수가 실행됨
    room_list = models.Room.objects.all()
    # orphans : 마지막 페이지에 존재하는 객체들
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={"page": rooms})
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")

    # page key에 대한 값을 가져옴 없는 경우 기본값 0
    # url에서 오는 것은 get request
    # [offset:limit]
    # context는 html로 변수를 넘겨줌 context={"template에서의 변수명": 값}