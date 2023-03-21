
from apps.models import *
from django.contrib.auth.models import User
def platrform_data_check_and_create_new_data(data):
    response={}
    user_id=data.get('user')
    platform_credentials_id = data.get('credentials')
    platform_settings_id = data.get('settings')

    if not User.objects.filter(id=user_id).exists():
        response['massage']="user id not exists"
        response['status'] =False
        response['data'] = []
        return response
    

    
    if not PlatformCredentials.objects.filter(id=platform_credentials_id).exists():
        response['massage'] = "platform_credentials id not exists"
        response['status'] = False
        response['data'] = []
        return response


    
    if not PlatformSettings.objects.filter(id=platform_settings_id).exists():
        response['massage'] = "platform_settings id not exists"
        response['status'] = False
        response['data'] = []
        return response

    


    response['massage'] = "OK"
    response['status'] = True
    response['data'] = data
    return response



