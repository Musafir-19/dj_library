import requests
from django.shortcuts import render


def search_page(request):
    query = request.POST.get("search_field")
    res = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q={query}').json()
    for value in res["items"]:
        book_title = value["volumeInfo"]["title"]
        book_author = value["volumeInfo"]["authors"][0]
        date = value["volumeInfo"]["publishedDate"]
        datadict = {'title': book_title, 'author': book_author,
                    'date': date}
        print(datadict)
    return render(request, 'search/results.html', {'datadict': datadict})
