from rest_framework.views import APIView
from apps.home.serializers import *
from apps.models import *
from .services.DataBaseServices import *
from .services.GenralServices import *
from .response import *

class PlatformCredentialsView(APIView):
    def post(self, request):

        if not PlatformCredentials.objects.filter(token_secret=request.data.get('token_secret')).exists():

            platform_credentials_serialized_data=PlatformCredentialsSerializer(data=request.data)

            if platform_credentials_serialized_data.is_valid():

                platform_credentials_serialized_data.save()

                return jsonResponse(status_code=200, massage="Platform Credentials Created", data=platform_credentials_serialized_data.data)

            return jsonResponse(status_code=400, massage="Platform Credentials Not Created", data=[])

        return jsonResponse(status_code=400, massage="Platform Credentials already exists", data=[])


class PlatformSettingsView(APIView):
    def post(self, request):

        # if not PlatformCredentials.objects.filter(token_secret=request.data.get('token_secret')).exists():

        platform_settings_serialized_data=PlatformSettingsSerializer(data=request.data)

        if platform_settings_serialized_data.is_valid():

            platform_settings_serialized_data.save()

            return jsonResponse(status_code=200, massage="Platform settings Created", data=platform_settings_serialized_data.data)

        return jsonResponse(status_code=400, massage="Platform settings Not Created", data=[])

        # return jsonResponse(status_code=400, massage="Platform Credentials already exists", data=[])

class PlatformView(APIView):
    def post(self, request):

        # if not PlatformCredentials.objects.filter(token_secret=request.data.get('token_secret')).exists():

        response_data=platrform_data_check_and_create_new_data(request.data)

        if response_data['status']:


            platform_serialized_data=PlatformSerializer(data=request.data)

            if platform_serialized_data.is_valid():

                platform_serialized_data.save()

                return jsonResponse(status_code=200, massage="Platform  Created", data=platform_serialized_data.data)

            return jsonResponse(status_code=400, massage="Platform  Not Created", data=[])

        return jsonResponse(status_code=400, massage=response_data['massage'], data=[])

        # return jsonResponse(status_code=400, massage="Platform Credentials already exists", data=[])