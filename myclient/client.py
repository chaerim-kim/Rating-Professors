import requests
import json
import pandas

# To check login status
loggedin = 0
baseurl = 'http://127.0.0.1:8000/api'
# baseurl = 'http://sc17crk.pythonanywhere.com/api'

def main():
    while True:
        print("\n\nPlease select the command to execute.")
        print("1. To register, type 'register'")
        print("2. To login, type 'login url', with required argument(s).")
        print("3. To logout, type 'logout'")
        print("4. To view a list of all module instances and the professors, type 'list'")
        print("5. To view the rating of all professors, type 'view'")
        print(
            "6. To view the average rating of a certain professor in a certain module, type 'average professor_id module_code' with required argument(s).")
        print(
            "7. To rate the teaching of a certain professor in a cetain module, type 'rate professor_id module_code year semester rating'with required argument(s).")
        print("\n")

        option = input("Please select the menu : ")
        userinput = option.split()

        if userinput[0] == 'register':
            register()

        elif userinput[0] == 'login':
            if len(userinput) == 2:
                login(userinput[1])
            else:
                print('Specify login url.')

        elif userinput[0] == 'logout':
            logout()

        elif userinput[0] == 'list':
            list()

        elif userinput[0] == 'view':
            view()

        elif userinput[0] == 'average':
            if len(userinput) == 3:
                average(userinput[1], userinput[2])
            else:
                print('Specify the professor ID and module code.')

        elif userinput[0] == 'rate':
            if len(userinput) == 6:
                rate(userinput[1], userinput[2], userinput[3], userinput[4], userinput[5])
            else:
                print('Specify the professor ID, module code, year, semester and rating.')


def register():
    session = requests.Session()

    # prompt the user for details
    username = input("Enter username : ")
    email = input("Enter email : ")
    password = input("Enter password : ")

    # send a request to api along with data
    # url = 'http://sc17crk.pythonanywhere.com/api/register/'
    url = baseurl + '/register/'
    post_data = {
        'username': username,
        'email': email,
        'password': password
    }

    # send a request to api
    r = session.post(url, data=post_data)
    # print(r.status_code)
    print(r.content)


def login(user_url):
    global loggedin

    session = requests.Session()

    # prompt the user for deatils
    username = input("Enter username : ")
    password = input("Enter password : ")

    # send a request to api along with data
    url = user_url+'api/login/'
    post_data = {
        'username': username,
        'password': password
    }

    # send a request to api
    r = session.post(url, data=post_data)

    if r.status_code == 200:
        loggedin = 1

    print(r.content)
    # print(r.status_code)


# send logout request
def logout():
    global loggedin

    session = requests.Session()

    url = baseurl + '/logout/'
    r = session.get(url)

    loggedin = 0
    # print(r.status_code)
    print(r.content)


def list():
    session = requests.Session()

    # sending request
    url = baseurl + '/list/'
    r = session.get(url)

    # parsing objects
    parsed = json.loads(r.text)
    module_list = parsed['module_list']

    print_list = []
    for i in module_list:
        moduleobjects = {
            'Code': i.get('module_code'),
            'Name': i.get('name'),
            'Year': i.get('year'),
            'Semester': i.get('semester'),
            'Professor': i.get('professor_id') + ', Professor ' + i.get('first_name') + '. ' + i.get('last_name')
        }

        print_list.append(moduleobjects)

    print("=" * 80)

    print(pandas.DataFrame(print_list).reindex(
        columns=['Code', 'Name', 'Year', 'Semester', 'Professor']))

    print("=" * 80)

    # print(r.status_code)


def view():
    session = requests.Session()

    # send request
    url = baseurl + '/view/'
    r = session.get(url)

    # parsing objects
    parsed = json.loads(r.text)
    rating_list = parsed['rating_list']

    for i in rating_list:
        rating = i.get('rating')
        code = i.get('code')

        if code == 'JE1':
            first = 'J'
            last = 'Excellent'

        elif code == 'TT1':
            first = 'T'
            last = 'Terrible'

        elif code == 'VS1':
            first = 'V'
            last = 'Smart'

        print("The rating of Professor {0}. {1} ({2}) is {3}.".format(first, last, code, rating))

    # print(r.status_code)


def average(professor_id, module_code):
    session = requests.Session()

    # send a request to api along with data
    url = baseurl + '/average/'
    post_data = {
        'professor_id': professor_id,
        'module_code': module_code
    }
    # send a request to api
    r = session.post(url, data=post_data)

    parsed = json.loads(r.text)
    rating__avg = parsed['average_rating']

    print("The rating of Professor {0} in module {1} is {2}.".format(professor_id, module_code, rating__avg))
    # print(r.status_code)


def rate(professor_id, module_code, year, semester, rating):
    global loggedin

    if loggedin == 1:
        session = requests.Session()

        # send a request to api along with data
        url = baseurl + '/rate/'
        post_data = {
            'professor_id': professor_id,
            'module_code': module_code,
            'year': year,
            'semester': semester,
            'rating': rating
        }

        # send a request to api
        r = session.post(url, data=post_data)
        # print(r.status_code)
        print(r.content)

    else:
        print('You have to log in to rate.')


if __name__ == "__main__":
    main()
