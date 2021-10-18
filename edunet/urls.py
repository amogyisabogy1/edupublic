from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:profile>", views.dashboard, name="dashboard"),
    path("activelisting", views.activelisting, name="activelisting"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("viewlisting/<int:product_id>", views.viewlisting, name="viewlisting"),
    path("addtowatchlist/<int:product_id>",
         views.addtowatchlist, name="addtowatchlist"),
    path("addcomment/<int:product_id>", views.addcomment, name="addcomment"),
]
