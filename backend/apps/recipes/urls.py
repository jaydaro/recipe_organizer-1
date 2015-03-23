from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('',
    url('^recipes/$', RecipeList.as_view(), name='recipe-list')
)
