from django.conf.urls import patterns, include, url
from crowler import views
 
urlpatterns = patterns('',
                       url(r'^set_url_on_db/', views.set_url_on_db, name='set_url_on_db'),
                       url(r'^find-word/', views.find_need_word, name='find_need_word'),
                       url(r'^parse-content/', views.parse_content_by_words, name='parse_content_by_words'),
                       url(r'^', views.crowler_main, name='crowler_main'),

)
