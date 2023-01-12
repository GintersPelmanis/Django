from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Recepie, Ingridient, Rating, Category
from django.db.models import Q
import json
from .form import RatingForm , RecipeFilterForm



def deserialize_tagify(json_data):
    tags = json.loads(json_data)
    return [tag['value'] for tag in tags]



def filter_recepies(product_names, min_calories=None, max_calories=None, category=None):
    if product_names is not None:
        queryset = Recepie.objects.filter(Q(ingridient__product__name__in=product_names)).distinct()
        print(queryset)
    else:
        queryset = Recepie.objects.all()
    max_calories = int(max_calories) if max_calories else None
    min_calories = int(min_calories) if min_calories else None
    if min_calories is not None or max_calories is not None:
        recipes = [recipe for recipe in queryset if min_calories <= recipe.total_calories() <= max_calories]
        queryset = Recepie.objects.filter(pk__in=[recipe.pk for recipe in recipes])
    if category is not '':
        category_list = [category]
        category_queryset = Category.objects.filter(name__in=category_list)
        queryset = queryset.filter(category__in=category_queryset)
    return queryset

# Create your views here.
def base(request):
    if request.method == 'POST':
        data = request.POST
        request.session['data'] = data
        return HttpResponseRedirect('/search/')
    return render(request, 'index.html')
    
def search(request):
    if request.method == 'POST':
        data = request.POST
    else:
        data = request.session['data']

    if data.get("tags"):
        product_names = deserialize_tagify(data.get("tags"))
    else:
        product_names = None
    min_calories = data.get("min")
    max_calories = data.get("max")
    category = data.get("category")
    queryset = filter_recepies(product_names,min_calories,max_calories,category)
    return render(request, 'search.html', {'recepies': queryset,'tags':data, 'categories':Category.objects.all})

def details(request, name):
    receipe = Recepie.objects.get(name=name)


    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['Rating']
            Rating.objects.create(recepie=receipe, rating=rating)
    else:
        form = RatingForm()

    ingredients = Ingridient.objects.filter(recepie_id=receipe)
    context = {'receipe': receipe, 'ingredients': ingredients, 'form': form}
    return render(request, 'details.html', context )


  