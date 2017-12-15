from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create/$', views.PostCreateApi.as_view(), name="createapi"),
    url(r'^$', views.PostListApi.as_view(), name="list"),
    url(r'^(?P<pk>[\w-])+/$', views.PostDetailApi.as_view(), name="detail"),
    url(r'^(?P<pk>[\w-])+/edit/$', views.PostUpdateApi.as_view(), name="update"),
    url(r'^(?P<pk>[\w-])+/delete/$', views.PostDestroyApi.as_view(), name="delete"),

    url(r'^(?P<slug>[\w-])+/$', views.PostDetailsApi.as_view(), name="det"),

]
