import requests
from apps.home.response import ApiResponse

def GetRequest(url,headers,data=None):

    response=requests.get(url=url,headers=headers)

    return ApiResponse(response_code=response.status_code,body=response.json(),headers=response.headers)

def PostRequest(url, headers, data=None):

    response = requests.get(url=url,data=data ,headers=headers)

    return ApiResponse(response_code=response.status_code, body=response.json(), headers=response.headers)