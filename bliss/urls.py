from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'), 
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^blog/new/$', views.blognew, name='blognew'),
	url(r'^blog/edit/(?P<pk>\d+)$', views.blogedit, name='blogedit'),
	url(r'^blog/detail/(?P<pk>\d+)$', views.blogdetail, name='blogdetail'),
	url(r'^genre/detail/(?P<pk>\d+)$', views.genredetail, name='genredetail'),
	url(r'^book/detail/(?P<pk>\d+)$', views.bookdetail, name='bookdetail'),
	url(r'^user/(?P<pk>\d+)$', views.user, name='user'),
	url(r'^blog/comment/(?P<pk>\d+)$', views.comment, name='comment'),
	url(r'^book/comment/(?P<pk>\d+)$', views.commentbook, name='commentbook'),
	url(r'^user/$', views.user, name='user'),
	url(r'^user/edit/$', views.edit, name='edit'),
	url(r'^user/blog/$', views.bloguser, name='bloguser'),
	url(r'^user/blog/deleteBlog/(?P<pk>\d+)$', views.deleteBlog, name='deleteBlog'),
	url(r'^user/deleteUser/', views.deleteUser, name='deleteUser'),
]