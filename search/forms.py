from django import forms


class SearchBook(forms.Form):
    search_field = forms.CharField(max_length=100)