from django.http import JsonResponse

from .models import Pizza


def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    if pizza:
        data = {
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description
        }

        return JsonResponse(data)
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Pizza not found'
        }, status=404)
