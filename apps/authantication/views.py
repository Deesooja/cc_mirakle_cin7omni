from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from apps.models import PlatformOrderLineItem
from apps.serializers import *

class UserAuthanticationLoginView(APIView):
    def get(self, request):
        print(request.user)
        data={'method':"get"}
        return JsonResponse(data)

    def post(self, request):
        data={"staus":False}
        username = request.data.get('user_name')
        password = request.data.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            data['staus']=True
        # serializer = PlatformOrderLineItemSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        return JsonResponse(data)

    def put(self, request, pk):
        data = {'method': "post"}
        # line_item = PlatformOrderLineItem.objects.get(pk=pk)
        # serializer = PlatformOrderLineItemSerializer(line_item, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data)
        return JsonResponse(data)

    def delete(self, request, pk):
        data = {'method': "post"}
        # line_item = PlatformOrderLineItem.objects.get(pk=pk)
        # line_item.delete()
        return JsonResponse(data)

class UserRegistrationView(APIView):
    def post(self, request):
        data = {"staus": False}
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['data']=serializer.data
            return JsonResponse(serializer.data)
        return JsonResponse(data)

class UserLogoutView(APIView):
    def get(self, request):

        logout(request)

        data={'method':"logout"}
        return JsonResponse(data)
