
from django.urls import path

from . import views

# name of app (IMPORTANT for referring to any of the urlconfs by name)
app_name = "polls"

# list of URlconfs
# Each defines a mapping from a URL pattern to a View function, and also names the urlconf
# Note that some of the view functions are methods of GenericView classes from over in views.py
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results
#     path("<int:question_id>/results", views.results, name="results"),
#     # ex: /polls/5/vote
#     path("<int:question_id>/vote", views.vote, name="vote")

# ]