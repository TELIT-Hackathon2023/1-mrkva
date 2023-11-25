from django.shortcuts import render
from django.http import JsonResponse

def test_api(request):
    data = {
        'message': 'Hello, this is a test API endpoint!',
        'status': 'success'
    }
    return JsonResponse(data)


# Create your views here.
