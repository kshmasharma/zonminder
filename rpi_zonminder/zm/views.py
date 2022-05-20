from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_mode(request):
    data = json.loads(request.body.decode("utf-8"))
    print(data)
    if request.method == 'POST' :
        command = { 'name':'kshma sharma'}
        return JsonResponse(command)
    return JsonResponse({'error ': 'Error'})


#{
 #   "camIP" : "192.168.1.2",
  #  "camPass" : "admin",
   # "camUser" : "admin",
    #"numOfCamera" : "4",
#    "camPort" : "554"
#}