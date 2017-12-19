from django.conf.urls import url
from cms import views

urlpatterns = [
    # schedule
    url(r'^schedule/$', views.schedule_list, name='schedule_list'),   # list of schedule
    url(r'^schedule/add/$', views.schedule_edit, name='schedule_add'),  # add new schedule
    url(r'^schedule/mod/(?P<schedule_id>\d+)/$', views.schedule_edit, name='schedule_mod'),  # modify schedule
    url(r'^schedule/del/(?P<schedule_id>\d+)/$', views.schedule_del, name='schedule_del'),   # delete schedule
    url(r'^discussion/(?P<schedule_id>\d+)/$', views.DiscussionList.as_view(), name='discussion_list'),  #list of discussion
    url(r'^discussion/add/(?P<schedule_id>\d+)/$', views.discussion_edit, name='discussion_add'),        # add discussion
    url(r'^discussion/mod/(?P<schedule_id>\d+)/(?P<discussion_id>\d+)/$', views.discussion_edit, name='discussion_mod'), # modify discussion
    url(r'^discussion/del/(?P<schedule_id>\d+)/(?P<discussion_id>\d+)/$', views.discussion_del, name='discussion_del'), # delete discussion
]