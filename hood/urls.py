from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
        url('^$', views.index, name = 'index'),
        url(r'^home$', views.home, name = 'home'),
        url(r'^accounts/profile/$', views.profile, name = 'profile'),
        url(r'^services$', views.services, name = 'services'),
        url(r'^business$', views.business, name = 'business'),
        url(r'^about$', views.about, name = 'about'),
        url(r'^admin$', views.admin, name = 'admin')
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
