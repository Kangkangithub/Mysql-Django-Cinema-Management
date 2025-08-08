from django.shortcuts import render, redirect, get_object_or_404
from app01.models import Schedule
from app01.srcs.forms.form import ScheduleModelForm, ScheduleModelFormEdit
from app01.utils.page_nav import PageNav

# 排片列表
def schedule_list(req):
    search_data = req.GET.get("q", "")
    queryset = Schedule.objects.select_related("movie", "hall").all()

    if search_data:
        queryset = queryset.filter(movie__title__icontains=search_data)

    page_nav_obj = PageNav(req, queryset)
    page_queryset = page_nav_obj.page_queryset
    page_nav_string = page_nav_obj.get_html()

    content = {
        "queryset": page_queryset,
        "search_data": search_data,
        "page_nav_string": page_nav_string,
    }
    return render(req, "schedules/schedule_list.html", content)

# 添加排片
def schedule_add(req):
    if req.method == "GET":
        form = ScheduleModelForm()
        return render(req, "schedules/schedule_add.html", {"form": form})

    form = ScheduleModelForm(data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/schedules/list")

    return render(req, "schedules/schedule_add.html", {"form": form})

# 编辑排片
def schedule_edit(req, nid):
    obj = get_object_or_404(Schedule, schedule_id=nid)

    if req.method == "GET":
        form = ScheduleModelFormEdit(instance=obj)
        return render(req, "schedules/schedule_edit.html", {"form": form})

    form = ScheduleModelFormEdit(instance=obj, data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/schedules/list")

    return render(req, "schedules/schedule_edit.html", {"form": form})

# 删除排片
def schedule_delete(req):
    nid = req.GET.get("nid")
    Schedule.objects.filter(schedule_id=nid).delete()
    return redirect("/schedules/list")
