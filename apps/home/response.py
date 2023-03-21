from django.http import JsonResponse

def jsonResponse(status_code,massage,data):
    response={}
    response['status_code']=status_code
    response['massage'] = massage
    response['data'] = data
    return JsonResponse(response)