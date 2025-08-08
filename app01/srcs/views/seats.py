from django.shortcuts import render, redirect, get_object_or_404
from app01.models import Seat, Hall, Schedule


# 座位列表
def seat_list(request):
    queryset = Seat.objects.select_related("hall", "schedule").all()
    return render(request, "seat/seat_list.html", {"queryset": queryset})


# 添加座位
def seat_add(request):
    if request.method == "GET":
        halls = Hall.objects.all()
        schedules = Schedule.objects.all()
        return render(request, "seat/seat_add.html", {
            "halls": halls,
            "schedules": schedules
        })
    else:
        Seat.objects.create(
            seat_id=request.POST.get("seat_id"),
            seat_number=request.POST.get("seat_number"),
            status=int(request.POST.get("status", 0)),
            hall_id=request.POST.get("hall_id"),
            schedule_id=request.POST.get("schedule_id")
        )
        return redirect("/seat/list")


# 编辑座位
def seat_edit(request, nid):
    seat = get_object_or_404(Seat, seat_id=nid)

    if request.method == "GET":
        halls = Hall.objects.all()
        schedules = Schedule.objects.all()
        return render(request, "seat/seat_edit.html", {
            "seat": seat,
            "halls": halls,
            "schedules": schedules
        })
    else:
        seat.seat_number = request.POST.get("seat_number")
        seat.status = int(request.POST.get("status", 0))
        seat.hall_id = request.POST.get("hall_id")
        seat.schedule_id = request.POST.get("schedule_id")
        seat.save()
        return redirect("/seat/list")


# 删除座位
def seat_delete(request):
    nid = request.GET.get("nid")
    Seat.objects.filter(seat_id=nid).delete()
    return redirect("/seat/list")
