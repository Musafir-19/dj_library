import requests
# from django.db.models import Q
from django.shortcuts import render
from search.forms import SearchBook


def search_page(request):
    if request.method == 'POST':
        form = SearchBook(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get("search_field")
            res = requests.get(
                f'https://www.googleapis.com/books/v1/volumes?q={data}').json()
            for value in res["items"]:
                book_title = value["volumeInfo"]["title"]
                book_author = value["volumeInfo"]["authors"][0]
                date = value["volumeInfo"]["publishedDate"]
                datadict = {'title': book_title, 'author': book_author,
                            'date': date}
                print(datadict)
            return render(request, 'search/results.html', datadict)
    else:
        form = SearchBook()
        return render(request, 'index.html', {'form':form})


# def SearchPage(request):
#     query = request.get('search_but')
#     dbvalid = Book.objects.filter(
#         Q(title__contains=query) | Q(author__contains=query))
#     if dbvalid:
#         return dbvalid
#     else:
#         res = requests.get(
#             f'https://www.googleapis.com/books/v1/volumes?q={query}').json()
#         for value in res["items"]:
#             book_title = value["volumeInfo"]["title"]
#             book_author = value["volumeInfo"]["authors"][0]
#             date = value["volumeInfo"]["publishedDate"]
#         datadict = {'title': book_title, 'author': book_author,
#                     'date': date}
#         return render(request, 'search/results.html', datadict)


# class SearchPage(ListView):
#     model = Book
#     template_name = 'search/results.html'

#     def get_queryset(self):
#         query = self.request.GET.get('search_but')
#         object_list = Book.objects.filter(
#             Q(title__icontains=query) | Q(author__icontains=query))
#         if object_list:
#             return object_list
#         else:
#             res = requests.get(
#                 f'https://www.googleapis.com/books/v1/volumes?q={query}').json()
#             for value in res["items"]:
#                 book_title = value["volumeInfo"]["title"]
#                 book_author = value["volumeInfo"]["authors"][0]
#                 date = value["volumeInfo"]["publishedDate"]
#                 datadict = {'title': book_title, 'author': book_author,
#                             'date': date}
#                 print(datadict)
#                 return render(request, 'search/results.html',
#                               {'title': book_title, 'author': book_author, 'date': date})
