from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse


class IndexView(View):
    # template_name = "index.html"

    def get(self, request):
        return HttpResponse("Welcome to StartUpGuwahati!")
