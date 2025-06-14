from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import reviewForm

def review(request):
    if request.method == "POST":
        form = reviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank_you')
    else:
        form = reviewForm()
    return render(request, "reviews/review.html", {
        "form" : form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
