
from django.db.models import F # django object that refers to a FIELD in the database
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic


# View function for the homepage
def homepage(request):
    return render(
        request,
        "index.html",
        {
            "current_time": timezone.now()
        }
    )
