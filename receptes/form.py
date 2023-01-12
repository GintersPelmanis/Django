from django import forms
from .models import Category


class RatingForm(forms.Form):
    Rating = forms.IntegerField(min_value=1, max_value=10, initial=5)


class RecipeFilterForm(forms.Form):
    Produkti = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'id': 'tags'}))
    min_calories = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_calories = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))