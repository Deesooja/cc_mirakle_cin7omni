from django.http import JsonResponse

def endpointResponse(status_code,massage,data):
    response={}
    response['status_code']=status_code
    response['massage'] = massage
    response['data'] = data
    return JsonResponse(response)

class ApiResponse:
    def __init__(self, response_code, body, headers=None):

        if headers is None:
            headers = []
        self.headers = headers

        if 199 <= response_code <= 299:
            self.isSuccess = True
            self.message = "Success"
        else:
            self.isSuccess = False
            self.message = "Error occurred"

        self.body = body
        self.status_code = response_code