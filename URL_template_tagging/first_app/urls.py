from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('ur',views.tagger,name = 'URL_template_tagger'),
    path('other',views.other,name = 'other_page'),
]
