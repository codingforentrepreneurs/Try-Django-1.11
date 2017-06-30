from django.conf.urls import url


from .views import (
    # restaurant_createview,
    # restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView

)
urlpatterns = [
    url(r'^create/$',  RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'$', RestaurantListView.as_view(), name='list'),
]
