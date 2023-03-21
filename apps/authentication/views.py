from rest_framework.views import APIView
# from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from apps.home.serializers import *
from apps.home.response import endpointResponse

class UserAuthanticationLoginView(APIView):

    def post(self, request):
        try:
            response_data=''

            username = request.data.get('user_name')

            password = request.data.get('password')

            user=authenticate(request,username=username,password=password)

            if user:

                login(request,user)

                serializer = UserSerializer(data=user)

                if serializer.is_valid():

                    response_data=endpointResponse(status_code=200,massage="OK",data=serializer.data)

                response_data = endpointResponse(status_code=200, massage="OK", data=[])

            response_data = endpointResponse(status_code=400, massage="Credentials not match", data=[])

            return response_data

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])



class UserRegistrationView(APIView):
    def post(self, request):

        try:

            if not User.objects.filter(username=request.data.get('username')).exists():
                serializer = UserSerializer(data=request.data)

                if serializer.is_valid():

                    serializer.save()

                    return endpointResponse(status_code=200,massage="Registration Succesfully",data=serializer.data)
                # print(serializer.errors)
                return endpointResponse(status_code=400,massage="Not Registration Succesfully",data=[])

            return endpointResponse(status_code=400, massage="Username already exist", data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])

class UserLogoutView(APIView):
    def get(self, request):
        try:

            logout(request)

            return endpointResponse(status_code=200,massage="User Logout Succesfully",data=[])

        except Exception as e:

            return endpointResponse(status_code=500, massage=str(e), data=[])

