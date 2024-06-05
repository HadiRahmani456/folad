from django.urls import path
from . import views

app_name = 'news'
urlpatterns=[
    path('', views.posthome, name='post_list'),
    path('postdetail/<slug:post>/<int:pk>/', views.postdetail, name='post_detail'),
    path('postcategory/', views.PostCategory.as_view(), name='post_category'),
    path('relation/', views.relation, name='post_ralation'),
    path('videodetail/<slug:post>/<int:pk>/', views.videodetail, name='video_detail'),
    path('sliddetaill/<int:pk>/', views.sliddetail, name='slid_detail'),
    path('contactus/', views.contactus, name='contact_us'),
    path('videocategory/', views.videocategory, name='video_category'),

]