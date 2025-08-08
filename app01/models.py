from django.db import models
# Create your models here.
import datetime
from django.utils import timezone  # 导入时区工具


class Movie(models.Model):
    """影片表"""
    movie_id = models.BigAutoField(primary_key=True)

    title = models.CharField(verbose_name="影片名称", max_length=100)
    genre = models.CharField(verbose_name="影片类型", max_length=50, blank=True, default="")
    duration = models.PositiveIntegerField(verbose_name="影片时长（分钟）", null=True, blank=True)
    director = models.CharField(verbose_name="导演", max_length=100, blank=True, default="")
    cast = models.TextField(verbose_name="演员阵容", blank=True, default="")
    release_date = models.DateField(verbose_name="上映日期", null=True, blank=True)

    def __str__(self):
        return self.title

    
class Hall(models.Model):
    """影厅表"""
    hall_id = models.BigAutoField(primary_key=True, verbose_name="影厅编号")
    name = models.CharField(max_length=100, verbose_name="影厅名称")
    seat_count = models.PositiveIntegerField(verbose_name="座位总数")
    movie = models.ForeignKey(Movie, verbose_name="正在播放的影片", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    """用户表"""
    user_id = models.CharField(verbose_name="用户账号", primary_key=True, max_length=30)
    name = models.CharField(verbose_name="姓名", max_length=30, null=True, blank=True, default="")
    password = models.CharField(verbose_name="密码", max_length=64, null=True, blank=True, default="")
    age = models.IntegerField(verbose_name="年龄", null=True, blank=True, default=18)
    account = models.DecimalField(verbose_name="账户余额", decimal_places=2, max_digits=10, null=True, blank=True,
                                  default=0.0)
    creat_time = models.DateTimeField(verbose_name="入职时间", null=True, blank=True, default=datetime.datetime.now())
    gender_choices = ((1, "男"), (2, "女"))
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, null=True, blank=True)

    email = models.EmailField(verbose_name="邮箱", max_length=50, null=True, blank=True, default="")

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """排片管理"""
    schedule_id = models.BigAutoField(primary_key=True, verbose_name="排片编号")

    price = models.DecimalField(verbose_name="票价", decimal_places=2, max_digits=10, null=True, blank=True)

    show_time = models.DateTimeField(verbose_name="放映时间", null=True, blank=True)

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name="影片",
        to_field="movie_id",
        related_name="schedules"
    )

    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        verbose_name="影厅",
        to_field="hall_id",
        related_name="schedules"
    )

    def __str__(self):
        return f"{self.movie.title} - {self.hall.name} - {self.show_time.strftime('%Y-%m-%d %H:%M')}"


class Seat(models.Model):
    """座位表"""
    STATUS_CHOICES = (
        (0, "可用"),
        (1, "已预订"),
        (2, "已锁定"),
    )

    seat_id = models.CharField(primary_key=True, max_length=20, verbose_name="座位编号")
    seat_number = models.CharField(max_length=10, verbose_name="座位号")  # 如 A1、B5
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0, verbose_name="状态")

    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        verbose_name="影厅编号",
        to_field="hall_id",
        related_name="seats"
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        verbose_name="排片编号",
        to_field="schedule_id",
        related_name="seats"
    )

    def __str__(self):
        return f"{self.seat_number}（{self.get_status_display()}）"


class MyAdmin(models.Model):
    id = models.CharField(verbose_name="管理员账号", primary_key=True, max_length=32)
    user_name = models.CharField(verbose_name="管理员名", max_length=32)
    password = models.CharField(verbose_name="管理员密码", max_length=64)

    class Meta:
        verbose_name = "管理员"
        db_table = "管理员表"

    def __str__(self):
        return self.user_name


class Order(models.Model):
    oid = models.CharField(verbose_name="订单号", max_length=64, primary_key=True)
    title = models.CharField(verbose_name="名称", max_length=32, blank=True, null=True)
    price = models.DecimalField(verbose_name="价格", blank=True, null=True, decimal_places=2, max_digits=10)

    status_choices = (
        (1, "待支付"),
        (2, "支付中"),
        (3, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, blank=True, null=True)

    user = models.ForeignKey(
        verbose_name="用户编号",
        to="UserInfo",
        to_field="user_id",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    schedule = models.ForeignKey(
        verbose_name="排片编号",
        to="Schedule",
        to_field="schedule_id",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    seat = models.ForeignKey(
        verbose_name="座位编号",
        to="Seat",
        to_field="seat_id",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    buy_time = models.DateTimeField(verbose_name="购买时间", default=timezone.now)

    def __str__(self):
        return self.title

