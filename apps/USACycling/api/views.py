import requests
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd

from apps.USACycling.GoogleSheetAPI import GSheetAPI


class USACyclingProfileAPI(APIView):
    def post(self, request):
        get_token = requests.post('https://laravel-api.usacycling.org/api/v1/login', data=request.data)
        get_profile = requests.get('https://laravel-api.usacycling.org/api/v1/profile/self', cookies=get_token.cookies)
        try:
            value = []
            for i, j in get_profile.json().items():
                value.append(str(j))
            gs = GSheetAPI()
            # gs.get_values(gs.SPREADSHEET_ID, "A1:C2")
            gs.update_values(gs.SPREADSHEET_ID, 'Profile!A1:D2', "USER_ENTERED",
                             [
                                 value
                             ]
                             )
        except Exception as e:
            print(str(e))
        return Response(get_profile.json())


class ExportProfileAPI(APIView):
    def get(self, request):
        get_token = requests.post('https://laravel-api.usacycling.org/api/v1/login', data=request.query_params)
        get_profile = requests.get('https://laravel-api.usacycling.org/api/v1/profile/self', cookies=get_token.cookies)
        get_association = requests.get(
            'https://laravel-api.usacycling.org/api/v1/associations/local_association?address_id=17457',
            cookies=get_token.cookies)
        file_name = f"USACyclingProfile_{request.query_params.get('user_id', '-')}.xlsx"
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        try:
            pd.DataFrame([
                get_profile.json()
            ]).to_excel(writer, sheet_name='Profile', index=False)
            pd.DataFrame([
                get_association.json()
            ]).to_excel(writer, sheet_name='Associations', index=False)
        except Exception as e:
            print(str(e))
        writer.save()
        file = open(file_name, 'rb')
        return FileResponse(file)

class AssociationsAPI(APIView):
    def post(self, request):
        get_token = requests.post('https://laravel-api.usacycling.org/api/v1/login', data=request.data)
        get_profile = requests.get('https://laravel-api.usacycling.org/api/v1/associations/local_association?address_id=17457', cookies=get_token.cookies)
        try:
            value = []
            for i, j in get_profile.json().items():
                value.append(str(j))
            gs = GSheetAPI()
            # gs.get_values(gs.SPREADSHEET_ID, "A1:C2")
            gs.update_values(gs.SPREADSHEET_ID, 'Association!A1:D2', "USER_ENTERED",
                             [
                                 value
                             ]
                             )
        except Exception as e:
            print(str(e))
        return Response(get_profile.json())


class ZwiftProfileAPI(APIView):
    def post(self, request):
        get_token = requests.get(f'https://z00pbp8lig.execute-api.us-west-1.amazonaws.com/latest/zwiftId?username='+request.data.get('user_id')+'&pw='+request.data.get('user_password'))
        get_profile = requests.get(f"https://zwiftapi.weracehere.org/profile?zid={get_token.json()}")
        return Response(get_profile.json())