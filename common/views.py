from django.shortcuts import render


from datetime import datetime
from random import randint

from django.shortcuts import render
from django.views import View  # базовый класс
from django.http import HttpRequest, HttpResponse


class StringView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = """<h1>Hello, World</h1>"""

        return HttpResponse(now)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')   #django сама по умолчанию лезет в templates