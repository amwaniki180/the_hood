from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile',views.profile, name= 'profile'),
    url(r'^update',views.update_profile, name= 'update'),
    url(r'^update',views.create_profile, name= 'create'),
    url(r'^new_post',views.new_post ,name= 'new_post'),
    url(r'^add/neighbourhood',views.new_project, name= 'add_project'),
    url(r'^new_business',views.new_business ,name= 'new_business'),
    url(r'^project/(\d+)', views.project, name = "project"),
    url(r'^post/(\d+)', views.post, name = "post"),
    url(r'^new_post',views.new_post ,name= 'new_post'),
    url(r'^search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

