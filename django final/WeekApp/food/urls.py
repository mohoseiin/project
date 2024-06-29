from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodview, name='foodview'),
    # path("<int:year>/<int:month>/<int:day>/", views.searchweek),
    path("update/week/food/<int:id>", views.updatefood),
    path("update/week/food/<int:id>/access", views.accessupdatefood),

    path("update/buylist/<int:id>", views.buylistshow),
    path("update/buylist/<int:id>/access", views.accessbuylist),
]