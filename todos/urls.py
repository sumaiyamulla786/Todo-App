from django.conf.urls import url
from . import views

app_name = 'todos'

urlpatterns = [
    url(r'^$',views.todos_list,name='list'),
    url(r'^create/$',views.todos_create,name='create'),
    url(r'^about/$',views.todos_about,name='about'),
    url(r'^(?P<id>[\w-]+)/$',views.todos_detail,name='detail'),
    url(r'^update/(?P<id>[\w-]+)/$',views.todos_update,name='update'),
    url(r'^delete/(?P<id>[\w-]+)/$',views.todos_delete,name='delete'),
]