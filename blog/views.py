from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Review, Category
from .forms import PostForm, ReviewForm, CategoryForm, SearchForm


def index(request):
    # Obtenemos los valores de los parámetros de búsqueda
    query = request.GET.get("title")
    category = request.GET.get("category")

    print(f"Valor de búsqueda: {query}")

    posts = Post.objects.all()

    # Filtramos por título si se ingresó una búsqueda
    if query:
        posts = posts.filter(title__icontains=query)
        if len(posts) == 0:
            posts = Post.objects.all()

    # Filtramos por categoría si se proporcionó un ID de categoría (entero)
    if category and category.isdigit():
        posts = posts.filter(category_id=category)

    posts = posts.order_by("-date")

    search_form = SearchForm()

    return render(request, "index.html", {"posts": posts, "search_form": search_form})


def add_post(request):
    if request.method == "POST":
        form_inst = PostForm(request.POST)
        if form_inst.is_valid():
            form_inst.save()
            return redirect("blog:home")
        else:
            print(form_inst.errors)
    else:
        form_show = PostForm()
        return render(request, "add_post.html", {"posts": form_show})


def add_category(request):
    if request.method == "POST":

        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:home")
        else:
            print(form.errors)
    else:
        formCategory = CategoryForm()
    return render(request, "add_category.html", {"formCategory": formCategory})


def details_post(request, post_id):
    one_posts = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        # print(request.method)
        reviews_form = ReviewForm(request.POST)
        if reviews_form.is_valid():
            # Crea una nueva reseña
            review = reviews_form.save(commit=False)
            review.post = one_posts  # Asocia la reseña con el post actual
            review.save()  # Guarda la reseña en la base de datos
            return redirect("blog:details", post_id=post_id)

    else:
        reviews_form = ReviewForm()

    # Obtiene todas las reseñas para el post actual
    reviews = one_posts.reviews.all()

    return render(
        request,
        "details_post.html",
        {"one_posts": one_posts, "reviews_form": reviews_form, "reviews": reviews},
    )


# def search_post(request):
#     posts = f"aca buscamos por titulo"
#     return render(request, "search_post.html", {"posts": posts})
