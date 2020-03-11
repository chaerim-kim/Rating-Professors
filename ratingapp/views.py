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
from django.db.models import Count


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

    # from ratingapp.models import Professor, Module, Rating


    # # PRINTING PROFESSORRRRS
    # for mod in Module.objects.all():
    #     for prof in mod.taught_by.all():
    #         professor_id = prof.professor_id
    #         first_name = prof.first_name
    #         last_name = prof.last_name
    #         print (professor_id, first_name,last_name)


    # module_list = Module.objects.all().values()

    new_list = []
    for module in Module.objects.all():
        module_code = module.module_code
        name = module.name
        year = module.year
        semester = module.semester

        professor_id = module.taught_by.all().values('professor_id') # this gives a queryset
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

    return http_response


def HandleView(request):
    http_bad_response = HttpResponseBadRequest()
    http_bad_response['Content-Type'] = 'text/plain'

    if request.method != 'GET':
        http_bad_response.content = 'Only GET request is allowed'
        return http_bad_response

    new_list=[]
    for rate in Rating.objects.all():
        rating = rate.rating

        # accessing foreign key values
        first_name = rate.which_professor.first_name
        last_name = rate.which_professor.last_name
        code = rate.which_professor.professor_id

        ratingobjects = {
            'rating': rating,
            'first_name': first_name,
            'last_name': last_name,
            'code': code
        }
        new_list.append(ratingobjects)

    payload = {'rating_list': new_list}

    http_response = HttpResponse(json.dumps(payload))
    http_response['Content-Type'] = 'application/json'
    http_response.status_code = 200
    http_response.reason_phrase = 'OK'

    return http_response


def HandleAverage(request):
    if request.method == 'POST':
        user_professor_id = request.POST.get('professor_id')
        user_module_code = request.POST.get('module_code')


        rating_for_mod = Rating.objects.all()
        real = rating_for_mod.filter(which_professor.professor_id=user_professor_id, which_module.module_code=user_module_code)
        for i in rating_for_mod:
            i.filter(.professor_id=user_professor_id, which_module.module_code=user_module_code)
    # Author.objects.values('name').annotate(average_rating=Avg('book__rating'))

# @login_required
# def HandleRate(request):
