
from django.http import HttpResponse, JsonResponse

def home_page (request):
    print("Home Page request")
    data =["Hina", "Ibrahim", "Shahzad", "Jannat", "Arham"]
    return HttpResponse("<h1> Hello HOME PAGE </h1>")
    #return JsonResponse(data, safe=False)