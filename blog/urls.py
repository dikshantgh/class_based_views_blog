from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r"^$", views.PostListView.as_view(), name='list_posts'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.PostDetailView.as_view(), name='detail_posts'),

    url(r"^search/$", views.SearchListView.as_view(), name='search'),

    # url(r'^(?P<post_slug>[-\w]+)/share/$', views.EmailPostView.as_view(),name='post_share'),
    # url(r'^comment/', views.CommentView.as_view(), name='comment_add'),
]
