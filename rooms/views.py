from datetime import datetime
from django.shortcuts import render

# django가 발생한 request들을 python object로 변환하여 인자로 넘겨줌
def all_rooms(request):
    return render(request, "all_rooms.html")