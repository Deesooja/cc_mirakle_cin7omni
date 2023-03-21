from rest_framework.views import APIView
# from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from apps.home.serializers import *
from apps.home.response import jsonResponse

class UserAuthanticationLoginView(APIView):

    def post(self, request):
        response_data=''

        username = request.data.get('user_name')

        password = request.data.get('password')

        user=authenticate(request,username=username,password=password)

        if user:

            login(request,user)

            serializer = UserSerializer(data=user)

            if serializer.is_valid():

                response_data=jsonResponse(status_code=200,massage="OK",data=serializer.data)

            response_data = jsonResponse(status_code=200, massage="OK", data=[])

        response_data = jsonResponse(status_code=400, massage="Credentials not match", data=[])

        return response_data



class UserRegistrationView(APIView):
    def post(self, request):

        if not User.objects.filter(username=request.data.get('username')).exists():
            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():

                serializer.save()

                return jsonResponse(status_code=200,massage="Registration Succesfully",data=serializer.data)
            # print(serializer.errors)
            return jsonResponse(status_code=400,massage="Not Registration Succesfully",data=[])

        return jsonResponse(status_code=400, massage="Username already exist", data=[])

class UserLogoutView(APIView):
    def get(self, request):

        logout(request)

        return jsonResponse(status_code=200,massage="User Logout Succesfully",data=[])

