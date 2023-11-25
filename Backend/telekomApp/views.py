import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET
from django.conf import settings
import os


# Define the path to your JSON file
json_file_path = 'telekomApp/final.json'


def test_api(request):
    # Retrieve the URL parameter from the request
    url = request.GET.get('url', None)

    # Check if the URL parameter is provided
    if not url:
        return JsonResponse({'message': 'JSON data file not found.', 'status': 'error'})

    try:
        with open(json_file_path, 'r') as file:
            website_data = json.load(file)
            print("Data loaded successfully")  # Debugging log
    except Exception as e:
        print(f"Error reading file: {e}")  # Debugging log
        return JsonResponse({'message': 'Error reading JSON data.', 'status': 'error'})

    for entry in website_data:
        if entry['website_url'] == url:
            print("URL found")  # Debugging log
            return JsonResponse(entry)

    print("URL not found")  # Debugging log
    return JsonResponse({'message': 'URL not found in saved data.', 'status': 'not_saved'})



# Create your views here.
