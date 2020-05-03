from django.shortcuts import render
import json
from django.http import StreamingHttpResponse, JsonResponse
from .utils import look_up, keyword_search
from django.views.decorators.csrf import csrf_exempt
from .models import Stock
# Create your views here.

@csrf_exempt
def news_info(request):
    if request.method == 'POST':
         recv_data = json.loads(request.body)
         return JsonResponse(keyword_search(recv_data["stock"]), safe=False)
         #return_list =

@csrf_exempt
def lookup_info(request):
    if request.method == 'POST':
         recv_data = json.loads(request.body)
         return JsonResponse(look_up(recv_data["stock"], recv_data["range"], recv_data["interval"]), safe=False)
         #return_list =

@csrf_exempt
def ticker(request):
    print(Stock.objects.all().filter().values())
