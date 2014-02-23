from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.template.response import TemplateResponse
from seapp import views 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',  include(admin.site.urls)),
    url(r'^$',       views.home_page),
    url(r'^hello/$', views.hello),
)
handler404 = 'views.my_404_view'
handler400 = 'views.my_404_view'
