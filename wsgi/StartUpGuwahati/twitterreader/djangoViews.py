import requests

from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse


class IndexView(View):

    def get(self, request):
        r = requests.get("http://localhost:8000/api/twitterreader")
        rJson = r.json()
        for i in rJson['statuses']:
            return HttpResponse(i['text'])
