from django.conf.urls import include, url
from . import views
app_name = 'blog'
urlpatterns = [
	url(r'^$',views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/nuevo/$',views.post_nuevo,name='post_nuevo'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_editar, name='post_editar'),
]