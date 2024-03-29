from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.faq_monthly_by_number),
    path("<str:month>", views.monthly_faqs, name="month-faq")
]