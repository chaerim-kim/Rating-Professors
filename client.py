import os
import sys
import argparse
import json


# This parses the inputs from the command line!)
parser = argparse.ArgumentParser(description='Input a function!')

#  positional argument
parser.add_argument('option', help="Which function would you like to run?")

args = parser.parse_args()

if args.option == 'register':
    print("Register")

elif args.option == 'login':
    print("Login")


elif args.option == 'logout':
    print("Logout of current session")


elif args.option == 'list':
    print("list all module instances and the professors teaching each of them")

elif args.option == 'view':
    print("view  the rating of all professors")


elif args.option == 'average':
    print("average prof_id module_code")

elif args.option == 'rate':
    print("Rate professor_id module_code year semester rating")
