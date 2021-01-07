from datetime import datetime
from django.shortcuts import render
from . import models

# django가 발생한 request들을 python object로 변환하여 인자로 넘겨줌
# html내에서  변수를 사용하는법 : {{var}}
# logic 사용하는법 ex) for, if :  {%if%} {%else%} {%end if%}  {%for in%} {%end for%}
# 꼭 end를 사용해야함, indent는 하지 않아도 됨
def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    # page key에 대한 값을 가져옴 없는 경우 기본값 0
    # url에서 오는 것은 get request
    all_rooms = models.Room.objects.all()[offset:limit]
    # [offset:limit]
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
    # context는 html로 변수를 넘겨줌 context={"template에서의 변수명": 값}