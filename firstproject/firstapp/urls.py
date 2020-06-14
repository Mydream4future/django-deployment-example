from firstapp import views
from django.urls import path

# TEMPLATE TAGGING
app_name='firstapp'

urlpatterns=[
    path('base/',views.base,name='base'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative_url_templates,name='relative_url_templates'),
]
