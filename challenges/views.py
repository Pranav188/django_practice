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

def func_month(response, month):
    try:
        txt_str = monthly_challenges[month]
        txt_str_html = f"<h2>{txt_str}</h2>"
    except KeyError:
        return HttpResponseNotFound("nope")

    return HttpResponse(txt_str_html)
