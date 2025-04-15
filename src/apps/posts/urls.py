from django.urls import path, re_path
from .views import HomePageView, PostDetailView

app_name = 'posts'

urlpatterns = [
    re_path(r'^blog/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]
