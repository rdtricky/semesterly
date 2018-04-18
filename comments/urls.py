from django.conf.urls import patterns, url
from django.contrib import admin

import advisor.views

admin.autodiscover()

urlpatterns = patterns('',
    # viewer management
    url(r'^comments/addComment/$', comment.views.CommentView.as_view()),
    url(r'^comments/editComment/$', comment.views.CommentView.as_view()),
    url(r'^comments/getComments/(?P<sem_name>.+)/(?P<year>[0-9]{4})/(?P<tt_name>.+)/(?P<student_email>.+)/$',
                               comment.views.CommentView.as_view()),
    url(r'^comments/removeComment/(?P<comment_id>.+)/$', comment.views.CommentView.as_view()),
)
