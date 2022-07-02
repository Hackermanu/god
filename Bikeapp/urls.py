from django.urls import path
from Bikeapp.views import *

urlpatterns=[
    path('reg_page',reg_page),
    path('register',reg_details),

    path('bike_record',records),

    path('company',company_page),
    path('bike_company',display_cmpny),

    path('price',price_data),
    path('search_price',search_result)
    ]