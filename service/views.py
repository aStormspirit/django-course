from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

def page(request, page_num):
    return HttpResponse(f'{page_num}')