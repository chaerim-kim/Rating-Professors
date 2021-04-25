from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from .models import Professor, Module, Rating
import json
from decimal import *


def home():
    return HttpResponse('Homepage of COMP3011 Coursework 1')


@csrf_exempt
def HandleRegister(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        username = json_data.get('username')
        email = json_data.get('email')
        password = json_data.get('password')

        print(username, email, password)

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username=username, email=email, password=password)
            return HttpResponse('user created!')
        else:
            return HttpResponse('Username with that email or password already exists')
    print(request.data)
    return HttpResponse('connected to register! api!')


@csrf_exempt
def HandleLogin(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        username = json_data.get('username')
        password = json_data.get('password')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Login success for username: {0}'.format(username))
                # return HttpResponse(status=200)

            else:
                return HttpResponse("Your account is inactive.")
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

    new_list = []
    for module in Module.objects.all().order_by('module_code', 'semester'):
        module_code = module.module_code
        name = module.name
        year = module.year
        semester = module.semester

        professor_id = module.taught_by.all().values('professor_id')  # this gives a queryset
        professor_id2 = professor_id[0]['professor_id']

        first_name = module.taught_by.all().values('first_name')
        first_name2 = first_name[0]['first_name']

        last_name = module.taught_by.all().values('last_name')
        last_name2 = last_name[0]['last_name']

        moduleobjects = {
            'module_code': module_code,
            'name': name,
            'year': year,
            'semester': semester,
            'professor_id': professor_id2,
            'first_name': first_name2,
            'last_name': last_name2
        }

        new_list.append(moduleobjects)

    payload = {'module_list': new_list}

    http_response = HttpResponse(json.dumps(payload))
    http_response['Content-Type'] = 'application/json'
    http_response.status_code = 200
    http_response.reason_phrase = 'OK'

    # return http_response
    return JsonResponse(payload, status=200)


def HandleView(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'

    if request.method != 'GET':
        http_bad_response.content = 'Only GET request is allowed'
        return http_bad_response

    new_list = []
    prof_list = []
    for prof_id in Professor.objects.all().values('professor_id'):
        prof_id_get = prof_id.get('professor_id')
        prof_list.append(prof_id_get)

    for professor in prof_list:
        rating_prof = Rating.objects.filter(which_professor__professor_id=professor).aggregate(Avg('rating'))
        raw_rating = rating_prof.get('rating__avg')
        rounded = int(Decimal(raw_rating).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        ratingobjects = {
            'code': professor,
            'rating': rounded
        }
        new_list.append(ratingobjects)

    payload = {'rating_list': new_list}

    http_response = HttpResponse(json.dumps(payload))
    http_response['Content-Type'] = 'application/json'
    http_response.status_code = 200
    http_response.reason_phrase = 'OK'

    return http_response


@csrf_exempt
def HandleAverage(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        user_professor_id = json_data.get('professor_id')
        user_module_code = json_data.get('module_code')

        rating_for_mod = Rating.objects.filter(which_professor__professor_id=user_professor_id,
                                               which_module__module_code=user_module_code).aggregate(Avg('rating'))

        rat = rating_for_mod.get('rating__avg')
        rounded = int(Decimal(rat).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        payload = {'average_rating': rounded}

        http_response = HttpResponse(json.dumps(payload))
        http_response['Content-Type'] = 'application/json'
        http_response.status_code = 200
        http_response.reason_phrase = 'OK'

        return http_response


@csrf_exempt
def HandleRate(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        user_professor_id = json_data.get('professor_id')
        user_module_code = json_data.get('module_code')
        user_year = json_data.get('year')
        user_semester = json_data.get('semester')
        user_rating = json_data.get('rating')

        prof_search = Professor.objects.get(professor_id=user_professor_id)

        module_search = Module.objects.get(module_code=user_module_code,
                                           year=user_year,
                                           semester=user_semester,
                                           taught_by=prof_search)

        if prof_search is None or module_search is None:
            return HttpResponse("The module taught by the professor doesn't exist")

        else:
            Rating.objects.create(rating=user_rating,
                                  which_professor=prof_search,
                                  which_module=module_search)

            return HttpResponse('Rating created! ')

    return HttpResponse('Rating page')
