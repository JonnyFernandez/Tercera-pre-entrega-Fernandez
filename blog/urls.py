from django.urls import path
from .views import *

app_name = "blog"  # Asegúrate de que este nombre sea correcto

urlpatterns = [
    path("", index, name="home"),
    path("add_post/", add_post, name="post"),
    path("add_categoryyyyy/", add_category, name="category"),
    path("details_post/<post_id>", details_post, name="details"),
    # path("search_post/", search_post, name="search"),
]
