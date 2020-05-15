from django.http.response import HttpResponse
from demo.models import Book


def demo(request):
    data = Book.objects.filter(name='test')
    return HttpResponse('ok')
