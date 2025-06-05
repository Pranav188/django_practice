from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string



monthly_challenges = {
    "january": "no bitches?",
    "february": "lmao",
    "march": "tralaleo tralala",
    "april": "john pork",
    "may": "zesty",
    "june": "black ballz",
    "july": "birthday",
    "august": "no_video_games",
    "september": "where the huzz at?",
    "october" : "chopped bitches bday",
    "november" : "fein",
    "december" : None
}

def home_page(request):
    list_of_months = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        'month_name': months
    })





def func_month_number(response, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month number")
    redirect_month = months[month - 1]
    redirect_link = reverse('pranav_website', args=[redirect_month])
    return redirect(redirect_link)

def func_month(request, month):
    try:
        txt_str = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : txt_str,
            "month_name" : month
        })
    except KeyError:
        res = render_to_string('404.html')
        return HttpResponseNotFound(res)
