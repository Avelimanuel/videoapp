from . import views
from django.urls import path

urlpatterns=[
    path('',views.lobby,name='lobby'),
    path('room/',views.room,name='room'),
    path('get_token/',views.generateToken,name='get-token'),
    path('create_user/',views.createUser,name='create-member'),
    path('get_member/',views.getMember),
    path('delete_member',views.deleteMember)
]