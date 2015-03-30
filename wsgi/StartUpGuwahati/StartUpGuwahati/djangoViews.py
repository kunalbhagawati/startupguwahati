from django.views.generic import View
# from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader


class IndexView(View):
    # template_name = "index.html"

    def get(self, request):
        template = loader.get_template('StartUpGuwahati/index.html')
        context = RequestContext(request, {
            'title': "Welcome to StartUpGuwahati!",
        })
        return HttpResponse(template.render(context))
