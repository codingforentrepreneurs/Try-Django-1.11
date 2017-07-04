from django.conf.urls import url

from .views import ProfileDetailView, RandomProfileDetailView

urlpatterns = [
    url(r'^random/$', RandomProfileDetailView.as_view(), name='random'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
