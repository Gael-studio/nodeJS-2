from django.http import JsonResponse

# Create your views here.

def api_home(request, *args, **kwargs ):
    return JsonResponse({"massage": "hi there this is gael"})