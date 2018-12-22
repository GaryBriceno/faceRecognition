from django.conf.urls import url
from . import views

app_name = "website"

urlpatterns = [
    # post views
    url(r'^$',
        views.people_list,
        name="people_list"),

    url(r'^(?P<slug>[-\w]+)/$',
        views.people_details,
        name='people_detail'),
]

