from django.urls import path
from cgv.views import ActorView, MovieView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MovieView.as_view())
]
