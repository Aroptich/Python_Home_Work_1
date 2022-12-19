from UI import requests

def write_data(temp):
    with open('Test.txt', 'w', encoding="UTF-8") as text:
        for i in temp:
            text.writelines(i)


def read_data():
    with open('Test.txt', 'r') as reading_text:
        a = reading_text.readline()
        return a