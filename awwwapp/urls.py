from django.urls import path,re_path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



urlpatterns=[
  path('',views.home, name = 'home'),
  path('create_profile/',views.create_profile,name = 'create_profile'),
  re_path('profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
  path('create_project/',views.create_project,name = 'create_project'),
  path('disp_project/<project_id>',views.disp_project,name = 'disp_project'),
  path('search_project/',views.search_project,name = 'search_project'),
  path('email/', views.email, name='email'),
  re_path('edit_profile/<profile_id>',views.edit_profile,name='edit_profile'),



  # path('signup/', SignUpView.as_view(), name='signup'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)