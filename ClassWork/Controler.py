from UI import requests
import Functions
from DB import read_data


def click():



    if '+' in a:

        a, b = list(map(int, a.split('+')))
        print(Functions.sum(a, b))
    elif '-' in a:

        a, b = list(map(int, a.split('-')))
        print(Functions.difference(a, b))
    elif '*' in a:

        a, b = list(map(int, a.split('*')))
        print(Functions.multiply(a, b))
    elif '/' in a:

        a, b = list(map(int, a.split('/')))
        print(Functions.division(a, b))
