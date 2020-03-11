import requests
import json
import pandas


def main():
    # # This parses the inputs from the command line!)
    # parser = argparse.ArgumentParser(description='Input a function!')
    #
    # #  positional argument
    # parser.add_argument('option',   help="Which function would you like to run?")
    # # parser.add_argument('optional', nargs='+', dest='argvars', help="Which function would you like to run?")
    #
    # args = parser.parse_args()

    print("\n\nPlease select the command to execute.")
    print("1. To register: please type 'register'")
    print("2. To login: please type 'login url', with required argument(s).")
    print("3. To logout: type: 'logout'")
    print("4. To view a list of all module instances and the professors: type: 'list'")
    print("5. To view the rating of all professors : type'view'")
    print(
        "6. To view the average rating of a certain professor in a certain module: type: 'average professor_id module_code' with required argument(s).")
    print(
        "7. To rate the teaching of a certain professor in a cetain module: type: 'rate professor_id module_code year semester rating'with required argument(s).")
    print("\n")

    option = input("Please select the menu : ")

    if option == 'register':
        register()

    elif option == 'login':
        login()

    elif option == 'logout':
        logout()

    elif option == 'list':
        list()

    elif option == 'view':
        view()

    elif option == 'average':
        average()

    elif option == 'rate':
        rate()


# !!!!!!!!! simply displays the data returned by the service in a human readable format.
# send request AND
# process the response
# display to user


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


def login():
    # prompt the user for deatils
    username = input("Enter username : ")
    password = input("Enter password : ")

    # send a request to api along with data
    url = 'http://127.0.0.1:8000/api/login/'
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


def average():
    professor_id = input("Enter professor id : ")
    module_code = input("Enter module code : ")

    # send a request to api along with data
    url = 'http://127.0.0.1:8000/api/average/'
    post_data = {
        'professor_id': professor_id,
        'module_code': module_code
    }

    # send a request to api
    r = requests.post(url, data=post_data)
    print(r.status_code)


# def rate():
#     professor_id, module_code,year,semester,rating = input("Enter professor_id, module_code,year,semester,rating : ").split()
#
#     # send a request to api along with data
#     url = 'http://127.0.0.1:8000/api/rate/'
#     post_data = {
#         'professor_id': professor_id,
#         'module_code': module_code,
#         'year': year,
#         'semester': semester,
#         'rating': rating
#     }
#
#     # send a request to api
#     r = requests.post(url, data=post_data)
#     print(r.status_code)


if __name__ == "__main__":
    main()
