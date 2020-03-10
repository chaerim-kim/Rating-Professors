from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.http import (HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
                         HttpResponseServerError)
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Professor, Module, Rating
import json
from django.http import JsonResponse


def home(request):
    return HttpResponse('Hello, World!')


@csrf_exempt
def HandleRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username=username, email=email, password=password)
            return HttpResponse('user created!')
        else:
            return HttpResponse('Username with that email or password already exists')

    return HttpResponse('connected to register! api!')


@csrf_exempt
def HandleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Login success for username: {0}'.format(username))

            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details supplied for username: {0}".format(username))

    return HttpResponse("Login page")


def HandleLogout(request):
    logout(request)
    return HttpResponse("User logged out")


@csrf_exempt
def HandleList(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'

    if request.method != 'GET':
        http_bad_response.content = 'Only GET request is allowed'
        return http_bad_response


    # for valid requests
    module_list = Module.objects.all().values('module_code', 'name', 'year', 'semester', 'taught_by')

    mod = Module.objects.all()
    prof = mod.taught_by.all()
    print(prof)
    # prof2 = prof.professor_set.value('professor_id')
    # print(prof2)

    # if module code, year, semester is the same, combine it into one!!
    # Professor.objects.filter()


    new_list = []
    for module in module_list:
        moduleobjects = {
            'module_code': module.get('module_code'),
            'name': module.get('name'),
            'year': module.get('year'),
            'semester': module.get('semester'),
            'taught_by': module.get('taught_by')
        }

        new_list.append(moduleobjects)

    payload = {'module_list': new_list}

    http_response = HttpResponse(json.dumps(payload))
    http_response['Content-Type'] = 'application/json'
    http_response.status_code = 200
    http_response.reason_phrase = 'OK'

    return http_response



def HandleView(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'

    if request.method != 'GET':
        http_bad_response.content = 'Only GET request is allowed'
        return http_bad_response

    prof_rating = Rating.objects.all().values('which_professor', 'rating')

    # rr = Rating.objects.all()
    # whichhh = rr.professor.all() # this is fetching all professors from rating modell
    # print (whichhh)

    new_list = []
    for rating in prof_rating:
        ratingobjects = {
            # 'professor_id': rating.get('which_professor').get('professor_id'),
            # 'first_name': rating['which_professor']['first_name'],
            # 'last_name': rating['which_professor']['last_name'],
            'rating': rating.get('rating')
        }

        new_list.append(ratingobjects)
    print (new_list)

    payload = {'module_list': new_list}

    http_response = HttpResponse(json.dumps(payload))
    http_response['Content-Type'] = 'application/json'
    http_response.status_code = 200
    http_response.reason_phrase = 'OK'

    return http_response


def HandleAverage(request):
    if request.method == 'POST':
        professor_id = request.POST.get('professor_id')
        module_code = request.POST.get('module_code')

    #### SORT OUT HOW TO CALL SPECIFIC foreign key value

        # Rating.objects.filter(which_professor=professor_id, which_module=module_code)
        # Author.objects.values('name').annotate(average_rating=Avg('book__rating'))

# @login_required
# def HandleRate(request):

