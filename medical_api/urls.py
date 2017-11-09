from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from medical_api import views

urlpatterns = {
    url(r'^$', views.index, name='index'),  # Add this line
    url(r'^auth/', include('rest_framework.urls',  # ADD THIS URL
                           namespace='rest_framework')),
    url(r'^register/$', views.CreateUserView.as_view(),
        name='user'),  # Add this line
    url(r'^_token/', obtain_auth_token),  # Add this line
}

urlpatterns = format_suffix_patterns(urlpatterns)
