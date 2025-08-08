from django.shortcuts import render, redirect, get_object_or_404
from app01.models import Movie  # 修改为新的模型名

# 影片列表
def movie_list(request):
    queryset = Movie.objects.all()
    content = {
        "queryset": queryset,
    }
    return render(request, "movie/movie_list.html", content)

# 添加影片
def movie_add(request):
    if request.method == "GET":
        return render(request, "movie/movie_add.html")
    else:
        Movie.objects.create(
            title=request.POST.get("new_title", ""),
            genre=request.POST.get("genre", ""),
            duration=request.POST.get("duration") or None,
            director=request.POST.get("director", ""),
            cast=request.POST.get("cast", ""),
            release_date=request.POST.get("release_date") or None
        )
        return redirect("/movie/list")

# 删除影片
def movie_delete(request):
    nid = request.GET.get("nid")
    Movie.objects.filter(movie_id=nid).delete()
    return redirect("/movie/list")

# 编辑影片
def movie_edit(request, nid):
    movie = get_object_or_404(Movie, movie_id=nid)

    if request.method == "GET":
        content = {
            "movie_id": movie.movie_id,
            "title": movie.title,
            "genre": movie.genre,
            "duration": movie.duration,
            "director": movie.director,
            "cast": movie.cast,
            "release_date": movie.release_date.strftime("%Y-%m-%d") if movie.release_date else ""
        }
        return render(request, "movie/movie_edit.html", content)
    else:
        movie.title = request.POST.get("new_title", "")
        movie.genre = request.POST.get("genre", "")
        movie.duration = request.POST.get("duration") or None
        movie.director = request.POST.get("director", "")
        movie.cast = request.POST.get("cast", "")
        movie.release_date = request.POST.get("release_date") or None
        movie.save()
        return redirect("/movie/list")
