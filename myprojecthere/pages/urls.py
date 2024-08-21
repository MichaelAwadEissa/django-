from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'), 
    path('about/',views.about,name='about')   # new path for about page  # adding name to the URL for easy reference in templates  # when creating a new URL, always make sure to include a name for easy reference and debugging.  # name is used in template tag {% url 'name' %}.  # name should be unique in the project.  # name is used for URL resolution.  # it helps in keeping URLs clean and easy to understand.
]
