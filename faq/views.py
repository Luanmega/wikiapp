from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_faqs_dic = {
    "january": "january works",
    "february": "February works!!",
    "october": "October ok"
}

# Create your views here.


def faq_monthly_by_number(request, month):
    return HttpResponse(month)

#regresa texto por mes elegido en la url del sitio
def monthly_faqs(request, month):
    try:
        faq_text = monthly_faqs_dic[month]
        return HttpResponse(faq_text)
    except:
        return HttpResponseNotFound("This month is not supported!")