from django import forms

SEARCH_BY_TITLE = 'title'
SEARCH_BY_CONTRIBUTOR = 'contributor'


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=((SEARCH_BY_TITLE, 'Title'),
                                                         (SEARCH_BY_CONTRIBUTOR, 'Contributor')))
