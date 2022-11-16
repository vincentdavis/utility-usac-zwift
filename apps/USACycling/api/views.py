import requests
from rest_framework.response import Response
from rest_framework.views import APIView


class USACyclingProfileAPI(APIView):
    def post(self, request):
        get_token = requests.post('https://laravel-api.usacycling.org/api/v1/login', data=request.data)
        get_profile = requests.get('https://laravel-api.usacycling.org/api/v1/profile/self', cookies=get_token.cookies)
        return Response(get_profile.json())

class AssociationsAPI(APIView):
    def post(self, request):
        get_token = requests.post('https://laravel-api.usacycling.org/api/v1/login', data=request.data)
        get_profile = requests.get('https://laravel-api.usacycling.org/api/v1/associations/local_association?address_id=17457', cookies=get_token.cookies)
        return Response(get_profile.json())


class ZwiftProfileAPI(APIView):
    def post(self, request):
        get_token = requests.get(f'https://z00pbp8lig.execute-api.us-west-1.amazonaws.com/latest/zwiftId?username='+request.data.get('user_id')+'&pw='+request.data.get('user_password'))
        get_profile = requests.get(f"https://zwiftapi.weracehere.org/profile?zid={get_token.json()}")
        return Response(get_profile.json())