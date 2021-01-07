from math import ceil
from datetime import datetime
from django.shortcuts import render
from . import models

# django가 발생한 request들을 python object로 변환하여 인자로 넘겨줌
# html내에서  변수를 사용하는법 : {{var}}
# logic 사용하는법 ex) for, if :  {%if%} {%else%} {%end if%}  {%for in%} {%end for%}
# 꼭 end를 사용해야함, indent는 하지 않아도 됨
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    # page key에 대한 값을 가져옴 없는 경우 기본값 0
    # url에서 오는 것은 get request
    all_rooms = models.Room.objects.all()[offset:limit]
    # [offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
    # context는 html로 변수를 넘겨줌 context={"template에서의 변수명": 값}