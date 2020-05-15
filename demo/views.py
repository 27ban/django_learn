from django.http.response import HttpResponse
from demo.models import Book
from demo.tasks import add_task


def demo(request):
    obj = Book(name='中庸')
    obj.save()
    data = Book.objects.first()
    print(data.name)
    return HttpResponse('ok')


def do(request):
    res = add_task.delay(3, 8)
    return HttpResponse('%s' % res.taks_id)
