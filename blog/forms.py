from django import forms
from .models import Post, Review, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "category"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "description"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)


# class SearchForm(forms.Form):
#     q = forms.CharField(max_length=100, required=False, label="Buscar por título")
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(), required=False, label="Categoría"
#     )
