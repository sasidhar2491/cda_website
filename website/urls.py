from django.urls import path, re_path
# from .views import index,about_us
from . import views
app_name = "website"
urlpatterns = [
    path('',views.index,name='index'),
    path('about_us',views.about_us, name='about_us'),
    path('home',views.home, name='home'),
    path("profile_view/<slug:slug>", views.profile_view, name="profile_view"),
    path('profiles',views.profiles, name='profiles'),
    path('privacy_policy',views.privacy_policy, name='privacy_policy'),
    path('terms_conditions',views.terms_conditions, name='terms_conditions'),
    path('announcement',views.announcement, name='announcement'),
    path('contactus',views.contactus, name='contactus'),
    path('login',views.login, name='login'),
    path('get_profile_view',views.get_profile_view, name='get_profile_view'),
    # path('profile_view',views.profile_view,name='profile_view')

    # path('careers', views.careers, name='careers'),
    # path('contact_us', views.contact_us, name='contact_us'),
    # path('our_services', views.our_services, name='our_services'),
    # path('terms_policy', views.terms_policy, name='terms_policy'),
    # path('position_category/(?p<id>[\d]+)/$', views.position_category, name="position_category"),
    # re_path(r'^category/(?P<id>[\d]+)/$', views.service_category_details, name="service_category_details"),
    # re_path(r'^service/(?P<id>[\d]+)/$', views.service_details, name="service_details"),
    # re_path(r'^position_details/(?P<id>[\d]+)/$', views.position_details, name="position_details"),
]