from django import forms
from .models import Recipe, Tag, RecipeIngredient

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['id', 'author', 'title', 'is_active', 'tags']
        exclude = ['author', 'is_active']

    def __init__(self, *args, **kwargs):
        super(RecipeCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Recipe...',
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control tags',
        })

class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['id', 'author', 'title', 'is_active', 'tags']
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(RecipeUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Recipe...',
        })
        self.fields['is_active'].widget.attrs.update({
            'class': 'form-check-input',
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control tags',
        })

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Tag..',
        })


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
        exclude = ['recipe']

    def __init__(self, *args, **kwargs):
        super(RecipeIngredientForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingredient..',
        })
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['unit'].widget.attrs.update({
            'class': 'form-control',
        })
