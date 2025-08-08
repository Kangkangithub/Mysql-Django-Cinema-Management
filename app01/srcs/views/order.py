from django.shortcuts import render, redirect, get_object_or_404
from app01.models import Order, UserInfo, Schedule, Seat


# 订单列表
def order_list(request):
    queryset = Order.objects.select_related("user", "schedule", "seat").all()
    return render(request, "order/order_list.html", {"queryset": queryset})


# 添加订单
def order_add(request):
    if request.method == "GET":
        users = UserInfo.objects.all()
        schedules = Schedule.objects.all()
        seats = Seat.objects.all()
        return render(request, "order/order_add.html", {
            "users": users,
            "schedules": schedules,
            "seats": seats,
        })
    else:
        Order.objects.create(
            oid=request.POST.get("oid"),
            title=request.POST.get("title"),
            price=request.POST.get("price") or 0,
            status=int(request.POST.get("status", 1)),
            user_id=request.POST.get("user_id"),
            schedule_id=request.POST.get("schedule_id"),
            seat_id=request.POST.get("seat_id"),
            # buy_time 自动使用默认值，不用这里传
        )
        return redirect("/order/list")


# 编辑订单
def order_edit(request, oid):
    order = get_object_or_404(Order, oid=oid)

    if request.method == "GET":
        users = UserInfo.objects.all()
        schedules = Schedule.objects.all()
        seats = Seat.objects.all()
        return render(request, "order/order_edit.html", {
            "order": order,
            "users": users,
            "schedules": schedules,
            "seats": seats,
        })
    else:
        order.title = request.POST.get("title")
        order.price = request.POST.get("price") or 0
        order.status = int(request.POST.get("status", 1))
        order.user_id = request.POST.get("user_id")
        order.schedule_id = request.POST.get("schedule_id")
        order.seat_id = request.POST.get("seat_id")
        order.save()
        return redirect("/order/list")


# 删除订单
def order_delete(request):
    oid = request.GET.get("oid")
    Order.objects.filter(oid=oid).delete()
    return redirect("/order/list")
