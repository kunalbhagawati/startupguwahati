from twython import Twython

from rest_framework.views import APIView
from rest_framework.response import Response


class FetchResults(APIView):

    def get(self, request):
        APP_KEY = '5SraJUH4d4H2b5LjADeWhC3wW'
        APP_SECRET = 'FyPxiCPeHPtr6dxll6bgRi0xlnQGIKonATxkibv5SakP5jJbIS'

        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
        sRes = twitter.search(
                q='guwahati #guwahati :)', result_type='mixed', count=1)
        return Response(sRes, status=200)
