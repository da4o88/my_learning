from django.urls import path, re_path


from . import views

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$', views.topics, name='topics'),

    # Detail page for a single topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding new topic
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
]
