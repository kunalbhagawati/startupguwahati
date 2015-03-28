# from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# # REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', ])
def teapotView(request, potType):
    """
    Implements the HTCPCP (HyperText Coffee Pot Control Protocol)

    http://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol

    Sends back a standard 418 response code
    
    """
    
    if potType == '':
        potType = '1'

    potTypes = {
        '1' : " ◝(‿)𝀍 ", 
        '2' : " \{_}7 ", 
        '3' : " ◝⋃𝀍 ", 
        '4' : " ◝⋃⁊ ", 
        }

    response = ' Coffee at your service! ' + potTypes[potType]
    return Response(response, status=418)


class IndexView(TemplateView):
    def get(self, request):
        return HttpResponse("Welcome to StartUpGuwahati!")
