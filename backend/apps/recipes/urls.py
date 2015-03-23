from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url('^recipes/$', RecipeList.as_view(), name='recipe-list')
)
