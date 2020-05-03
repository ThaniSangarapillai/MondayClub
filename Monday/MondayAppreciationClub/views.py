from django.shortcuts import render
import json
from django.http import StreamingHttpResponse, JsonResponse
from .utils import look_up, keyword_search
# Create your views here.

def news_info(request):
    if request.method=='POST':
         recv_data = json.loads(request.body)
         print(recv_data)
         return JsonResponse([{"data":"Hello"}], safe=False)
         #return_list =
