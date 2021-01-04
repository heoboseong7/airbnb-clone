from datetime import datetime
from django.shortcuts import render
from . import models

# django가 발생한 request들을 python object로 변환하여 인자로 넘겨줌
# html내에서  변수를 사용하는법 : {{var}}
# logic 사용하는법 ex) for, if :  {%if%} {%else%} {%end if%}  {%for in%} {%end for%}
# 꼭 end를 사용해야함, indent는 하지 않아도 됨
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
    # context는 html로 변수를 넘겨줌 context={"template에서의 변수명": 값}