"""Learntest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from app01.srcs.views import movies, myadmin, schedules, user, account, order ,halls,seats

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("dbop", views.dbop),

    path("movie/list", movies.movie_list),
    path("movie/add", movies.movie_add),
    path("movie/<int:nid>/edit/", movies.movie_edit),
    path("movie/delete/", movies.movie_delete),

    path("hall/list", halls.hall_list),
    path("hall/add", halls.hall_add),
    path("hall/<int:nid>/edit", halls.hall_edit),
    path("hall/delete/", halls.hall_delete),

    path("user/list", user.user_list),
    path("user/add", user.user_add),
    path("user/delete/", user.user_delete),
    path("user/<nid>/edit/", user.user_edit),

    path("schedules/list", schedules.schedule_list , name='schedule_list'),
    path("schedules/add", schedules.schedule_add , name='schedule_add'),
    path("schedules/<int:nid>/edit", schedules.schedule_edit , name='schedule_edit'),
    path("schedules/delete/", schedules.schedule_delete , name="schedule_delete"),

    path('seat/list', seats.seat_list, name='seat_list'),
    path('seat/add', seats.seat_add, name='seat_add'),
    path('seat/edit/<str:nid>', seats.seat_edit, name='seat_edit'),
    path('seat/delete', seats.seat_delete, name='seat_delete'),

    path("myadmin/list", myadmin.myadmin_list),
    path("myadmin/add", myadmin.myadmin_add),
    path("myadmin/<nid>/edit/", myadmin.myadmin_edit),
    path("myadmin/delete/", myadmin.myadmin_delete),
    path("myadmin/<nid>/reset/", myadmin.myadmin_reset_pwd),

    path("login/", account.login),
    path("logout/", account.logout),

    path('order/list/', order.order_list, name='order_list'),
    path('order/add/', order.order_add, name='order_add'),
    path('order/edit/<str:oid>/', order.order_edit, name='order_edit'),
    path('order/delete/', order.order_delete, name='order_delete'),
]
