from django.http import HttpResponse
from django.http import (HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError,
                         )


def home(request):
    return HttpResponse('Hello, World!')


# def register(request):

