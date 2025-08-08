from django.shortcuts import render, redirect, get_object_or_404
from app01.models import Hall, Movie


# 影厅列表
def hall_list(request):
    queryset = Hall.objects.select_related("movie").all()
    return render(request, "hall/hall_list.html", {"queryset": queryset})


# 添加影厅
def hall_add(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        return render(request, "hall/hall_add.html", {"movies": movies})
    else:
        Hall.objects.create(
            name=request.POST.get("name", ""),
            seat_count=int(request.POST.get("seat_count") or 0),
            movie_id=request.POST.get("movie_id") or None
        )
        return redirect("/hall/list")


# 编辑影厅
def hall_edit(request, nid):
    hall = get_object_or_404(Hall, hall_id=nid)

    if request.method == "GET":
        movies = Movie.objects.all()
        return render(request, "hall/hall_edit.html", {
            "hall": hall,
            "movies": movies
        })
    else:
        hall.name = request.POST.get("name", "")
        hall.seat_count = int(request.POST.get("seat_count") or 0)
        hall.movie_id = request.POST.get("movie_id") or None
        hall.save()
        return redirect("/hall/list")


# 删除影厅
def hall_delete(request):
    nid = request.GET.get("nid")
    Hall.objects.filter(hall_id=nid).delete()
    return redirect("/hall/list")
