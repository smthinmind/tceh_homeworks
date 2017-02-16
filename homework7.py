
import requests
import json
import re


# Task 1:

def write_to_file(data):
    file_path = input('Input file path: ')
    my_file = open(file_path, 'w')
    my_file.write(data)
    my_file.close()


def read_file_data():
    file_path = input('Input file path: ')
    my_file = open(file_path, 'r')
    print(my_file.read())
    my_file.close()


if __name__ == '__main__':
    # input path - /Users/dmitry_korneychuk/Code/test_file_object.py
    write_to_file("print('Hey, I\'m writing directly to the file!')")
    read_file_data()


# Task 2:

def parse_url_headers():
    # Parse & print headers
    parsed_url = input('Input parsed url: ')
    headers = requests.get(parsed_url).headers
    print('Printing parsed keys and values:', '\n')
    for key, value in headers.items():
        print('{} = {}'.format(key, value))

    # Write json to file
    file_path = input('Input file path to write json: ')
    my_file = open(file_path, 'w')
    my_file.write(json.dumps(dict(headers)))
    my_file.close()


if __name__ == '__main__':

    parse_url_headers()
    # input url - https://jsonplaceholder.typicode.com/
    # input path - /Users/dmitry_korneychuk/Code/test_file_object.py


# Task 3:

if __name__ == '__main__':

    parsed_url = requests.get('https://habrahabr.ru/')
    content = str(parsed_url.content)

    # Refferal links pattern in requested body
    body_pattern = r'(a href="http[^\s]*\")'
    all_links = re.findall(body_pattern, content)

    # Format and print refferal links
    for i in all_links:
        link_pattern = r'(http[^\s]*[^\"])'
        ref_link = re.search(link_pattern, i)
        print(ref_link.group(), '\n')


# Task 4
