import requests
import json
import pandas
import sys


def main():
    if len(sys.argv) == 1:
        print('Invalid command - Enter your options.')

    elif sys.argv[1] == 'register':
        register()

    elif sys.argv[1] == 'login':
        if len(sys.argv) == 3:
            login(sys.argv[2])
        else:
            print ('Specify login url.')

    elif sys.argv[1] == 'logout':
        logout()

    elif sys.argv[1] == 'list':
        list()

    elif sys.argv[1] == 'view':
        view()

    elif sys.argv[1] == 'average':
        if len(sys.argv) == 4:
            average(sys.argv[2], sys.argv[3])
        else:
            print ('Specify the professor ID and module code.')

    elif sys.argv[1] == 'rate':
        if len(sys.argv) == 7:
            rate(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],sys.argv[6])
        else:
            print ('Specify the professor ID, module code, year, semester and rating.')



def register():
    # prompt the user for deatils
    username = input("Enter username : ")
    email = input("Enter email : ")
    password = input("Enter password : ")

    # send a request to api along with data
    url = 'http://127.0.0.1:8000/api/register/'
    post_data = {
        'username': username,
        'email': email,
        'password': password
    }

    # send a request to api
    r = requests.post(url, data=post_data)
    print(r.status_code)
    print(r.content)


def login(user_url):
    # prompt the user for deatils
    username = input("Enter username : ")
    password = input("Enter password : ")

    # send a request to api along with data
    # url = 'http://127.0.0.1:8000/api/login/'
    url = user_url
    post_data = {
        'username': username,
        'password': password
    }

    # send a request to api
    r = requests.post(url, data=post_data)
    print(r.status_code)
    print(r.content)


# send logout request
def logout():
    url = 'http://127.0.0.1:8000/api/logout/'
    r = requests.get(url)
    print(r.status_code)
    print(r.content)


def list():
    # sending request
    url = 'http://127.0.0.1:8000/api/list/'
    r = requests.get(url)

    # parsing objects
    parsed = json.loads(r.text)
    module_list = parsed['module_list']

    # print labels
    # print("{:<8} {:<8} {:<8} {:<15} {:<20}".format('Code', 'Name', 'Year', 'Semester', 'Taught by'))

    print_list = []
    for i in module_list:
        moduleobjects = {
            'Code': i.get('module_code'),
            'Name': i.get('name'),
            'Year': i.get('year'),
            'Semester': i.get('semester'),
            'professor_id': i.get('professor_id'),
            'first_name': i.get('first_name'),
            'last_name': i.get('last_name')
        }
        # print (moduleobjects)

        print_list.append(moduleobjects)

    print("=" * 90)

    # print(pandas.DataFrame(print_list, headers, headers))
    print(pandas.DataFrame(print_list).reindex(
        columns=['Code', 'Name', 'Year', 'Semester', 'professor_id', 'first_name', 'last_name']))

    print("=" * 90)

    print(r.status_code)


def view():
    # send request
    url = 'http://127.0.0.1:8000/api/view/'
    r = requests.get(url)

    # parsing objects
    parsed = json.loads(r.text)
    rating_list = parsed['rating_list']

    for i in rating_list:
        rating = i.get('rating')
        first = i.get('first_name')
        last = i.get('last_name')
        code = i.get('code')

        print("The rating of Professor {0}. {1} ({2}) is {3}.".format(first, last, code, rating))

    print(r.status_code)


def average(professor_id,module_code):

    # send a request to api along with data
    url = 'http://127.0.0.1:8000/api/average/'
    post_data = {
        'professor_id': professor_id,
        'module_code': module_code
    }

    # send a request to api
    r = requests.post(url, data=post_data)
    print(r.status_code)


def rate(professor_id, module_code, year, semester, rating):
    print('Not yert')

    # # send a request to api along with data
    # url = 'http://127.0.0.1:8000/api/rate/'
    # post_data = {
    #     'professor_id': professor_id,
    #     'module_code': module_code,
    #     'year': year,
    #     'semester': semester,
    #     'rating': rating
    # }
    #
    # # send a request to api
    # r = requests.post(url, data=post_data)
    # print(r.status_code)


if __name__ == "__main__":
    main()
