from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

item_lst = []
# Create your views here.
@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value', '')
            item_lst.append(value)
            print(item_lst)
            return JsonResponse({'status': 'success', 'received_value': value})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'failed', 'message': 'Only POST method is allowed'}, status=405)

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value', '')
            item_lst.remove(value)
            print(item_lst)
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'failed', 'message': 'Only DELETE method is allowed'}, status=405)
