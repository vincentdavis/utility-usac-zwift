import requests
from rest_framework.response import Response
from rest_framework.views import APIView


class USACyclingProfileAPI(APIView):
    def post(self, request):
        get_token = requests.post('https://laravel-api.usacycling.org/api/v1/login', data=request.data)
        get_profile = requests.get('https://laravel-api.usacycling.org/api/v1/profile/self', cookies=get_token.cookies)
        return Response(get_profile.json())