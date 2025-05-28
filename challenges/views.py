from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
monthly_challenges = {
    "jan": "no bitches?",
    "feb": "lmao",
    "mar": "tralaleo tralala",
    "apr": "john pork",
    "may": "zesty",
    "jun": "black ballz",
    "jul": "birthday",
    "aug": "bgmi",
    "sept": "where the huzz at?",
    "oct" : "chopped bitches bday",
    "nov" : "fein",
    "dec" : "xmas"
}

def func_month_number(response, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month number")
    redirect_month = months[month - 1]
    redirect_link = reverse('pranav_website', args=[redirect_month])
    return redirect(redirect_link)

def func_month(response, month):
    try:
        txt_str = monthly_challenges[month]
    except KeyError:
        return HttpResponseNotFound("nope")

    return HttpResponse(txt_str)
