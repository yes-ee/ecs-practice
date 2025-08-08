from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET'])
def index(request):
    return HttpResponse("안녕하세요! 클라우드 2기 이예슬입니다 ☺️")
