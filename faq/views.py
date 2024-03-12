from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_faqs_dic = {
    "january": "january works",
    "february": "February works!!",
    "october": "October ok"
}

# Create your views here.

def faq_monthly_by_number(request, month):
    months = list(monthly_faqs_dic.keys())

    if month > len(monthly_faqs_dic):
        return HttpResponseNotFound("Month not valid")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-faq", args=[redirect_month]) #how to build a full path -> /faq/january

    return HttpResponseRedirect(redirect_path)

#regresa texto por mes elegido en la url del sitio
def monthly_faqs(request, month):
    try:
        faq_text = monthly_faqs_dic[month]
        response_data = f"<h1>{faq_text}</h1>" #return html instead of plain text
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")