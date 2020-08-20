from django.http import JsonResponse

from .models import Pizza


def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    data = {
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description
    }

    return JsonResponse(data)
