# from django.conf.urls import  url
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

# We are adding a URL called /home
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage,name='login'),
   
    #path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    
    path('signup/', views.signupview, name='signup'),
    path('logout/',views.logoutView, name="logout"),

    path('reset_password/',views.password_reset_request, name="password_reset"),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name="password_reset_complete"),
 
]
urlpatterns+=staticfiles_urlpatterns()

#submit email form
# email sent success message
# link to password reset form in email
#password successfully changed message