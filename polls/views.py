
from django.db.models import F # django object that refers to a FIELD in the database
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Several classes on this page implement generic views
# The actual view function to be called is their as_view() method

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    # Tells the ListView that its list will be a list of five Questions
    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):    
    model = Question # Tells the DetailView that its object of interest will be the Question model
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question # Tells the DetailView that its object of interest will be the Question model
    template_name = "polls/results.html"


    


# View function for the vote page
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object. Try and grab the selected choice attached to it.
        # If there's no choice, it will throw a KeyError when you try to access it
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Selected invalid choice
        return render(
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            }
        )
    else:
        selected_choice.votes = F("votes") + 1 
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))




# # View function for the homepage
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     return render(
#         request,
#         "polls/index.html",
#         {
#             "latest_question_list": latest_question_list
#         }
#     )

# # View function for detail page
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# # View function for the results page
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})