from django.shortcuts import render
from elasticsearch_dsl import Search

# Create your views here.

def search(request):
    q = request.GET.get('q')
    response =''
    if q:
        response = Search().filter('term', author=q).execute()

    return render(request,'templates/search/search.html',{'response':response})
