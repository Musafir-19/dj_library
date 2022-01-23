import requests
from django.shortcuts import render
from books.models import Book


def search_page(request):
    query = request.POST.get("search_field")
    if  Book.objects.filter(title__contains=query):
        books = Book.objects.filter(title__contains=query)
    else:
        res = requests.get(
            f'https://www.googleapis.com/books/v1/volumes?q={query}').json()
        books = []
        for value in res["items"]:
            url = value["volumeInfo"]["previewLink"]
            book_title = value["volumeInfo"]["title"]
            try:
                book_author = value["volumeInfo"]["authors"][0]
                date = value["volumeInfo"]["publishedDate"]
            except:
                book_author = "Нет данных"
            datadict = {'title': book_title, 'author': book_author,
                        'date': date, 'url': url}
            books.append(datadict)
            print(books)
    return render(request, 'search/results.html', {'datadict': books})
