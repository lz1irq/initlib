import sys

import requests

API_FMT = 'https://www.googleapis.com/books/v1/volumes?q={isbn}'

def get_by_isbn(isbn):
    rq = requests.get(API_FMT.format(isbn=isbn))
    data = rq.json()
    book = data['items'][0]['volumeInfo']

    info = {
            'title': book['title'] + ' ' + book['subtitle'],
            'author': ','.join(book['authors']),
            'pages': book['pageCount'],
            'publisher': book['publisher'].strip('""'),
            'year': book['publishedDate'].split('-')[0]
            }

    return info

if __name__ == '__main__':
    print(get_by_isbn(sys.argv[1]))




