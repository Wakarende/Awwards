from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  path('',views.home, name = 'home'),
  path('create_profile/',views.create_profile,name = 'create_profile'),
  re_path('profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
  path('add_project/',views.create_project,name = 'create_project'),




  # path('signup/', SignUpView.as_view(), name='signup'),
  
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)