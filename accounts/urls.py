# from django.conf.urls import  url
from django.urls import path , include, reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

# We are adding a URL called /home
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage,name='login'),
    
    path('signup/', views.signupview, name='signup'),
    path('logout/',views.logoutView, name="logout"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="register/password_reset.html" ,success_url=reverse_lazy('accounts:password_reset_done'),email_template_name='register/password_reset_email.html'), name="password_reset"),

    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name="password_reset_done"),

    path("password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html',success_url=reverse_lazy('accounts:password_reset_complete')), name="password_reset_confirm"),

    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name="password_reset_complete"),
]
urlpatterns+=staticfiles_urlpatterns()

#submit email form
# email sent success message
# link to password reset form in email
#password successfully changed message