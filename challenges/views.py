from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
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
    "august": "bgmi",
    "september": "where the huzz at?",
    "october" : "chopped bitches bday",
    "november" : "fein",
    "december" : "xmas"
}

def home_page(response):
    list_of_months = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse('pranav_website', args=[month])
        list_of_months += f'<li><a href = \'{month_path}\'>{month}</a></li>'

    response_data = f'<ul>{list_of_months}</ul>'
    return HttpResponse(response_data)





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
            "month_name" : month.capitalize()
        })
    except KeyError:
        return HttpResponseNotFound("nope")
