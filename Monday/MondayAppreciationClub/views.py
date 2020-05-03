from django.shortcuts import render
import json
from django.http import StreamingHttpResponse, JsonResponse
from .utils import look_up, keyword_search, readtickerdata
from django.views.decorators.csrf import csrf_exempt
from .models import Stock
from django.core.exceptions import SuspiciousOperation

# Create your views here.

@csrf_exempt
def news_info(request):
    if request.method == 'POST':
         recv_data = json.loads(request.body)
         return JsonResponse(keyword_search(recv_data["stock"]), safe=False)
         #return_list =
    raise SuspiciousOperation("Invalid request; see documentation for correct paramaters")

@csrf_exempt
def lookup_info(request):
    print(request)
    #recv_data = json.loads(request.body)
    #print(recv_data)
    #return JsonResponse(look_up(recv_data["stock"], recv_data["range"], recv_data["interval"]), safe=False)
    #return_list =

@csrf_exempt
def ticker(request):
    records = Stock.objects.all()
    json_res = []
    count = 0
    for record in records:
        count += 1
        print(record.ticker, count)
        result = {"ticker":record.ticker, "name":record.company_name, "price":record.price}
        if count == 100:
            break
        if not result:
            continue

        json_res.append(result)

    return JsonResponse(json_res, safe=False)
