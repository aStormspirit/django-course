from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.template.loader import get_template
from django.shortcuts import render

from .models import Product

def index(request):
    return render(request, 'index.html')

def page(request, page_num):
    return HttpResponse(f'{page_num}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404('NOT FOUND')

    return HttpResponse('OK')

def file_show(request):
    file = 'service/photo.jpg'
    return FileResponse(open(file, 'rb'), as_attachment=True, filename='photo')

def json_show(request):
    data = {'cost': 130, 'title': 'book'}
    return JsonResponse(data)