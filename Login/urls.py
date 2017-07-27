from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = "Login"
urlpatterns = [
    url('^$',views.Login,name='Login'),
    url('^login$',views.Verify,name='verify_login'),
    url('^register$',views.Register,name='Register'),
    url('^logout$',views.Logout,name='Logout'),
    url('^user_details/(?P<username>[\w\-]+)$',views.user_details,name='User_Details'),
    url('^user_det$',views.user_det,name='User_Det'),
    url('^question_responses$',views.question_res,name='question_responses'),
    url('^Most_Compatible$',views.Most_Compatible,name='Most_Compatible'),
]
