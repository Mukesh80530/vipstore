from django.urls import path
from .views import dashboard, category, about, contact, faq

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("dashboard/", dashboard, name="dashboard"),
    path("category", category, name='sub-category'),

    path("about-us/", about, name="about-us"),
    path("contact/", contact, name='contact-us'),
    path("faq/", faq, name='faq')

]
