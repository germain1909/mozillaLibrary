"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')), # declare catlog pat
    path('', RedirectView.as_view(url='catalog/', permanent=True)), # 
    #path('accounts/', include('django.contrib.auth.urls')), #authorization
    #url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'), 
    #url(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'), 
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'), 
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'), 
    path('accounts/passwordreset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'), 
    path('accounts/passwordresetdone/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'), 
    path('accounts/passwordresetconfirm/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm_form.html"), name='password_reset_confirm'), 
    path('accounts/passwordresetcomplete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'), 
    # known bug you have to explicitly override logout
    # could create an explicit view for this
    #paths are case sensitive
    #cannot have any duplicate urls or duplicate name fields
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#Django does not serve static files like CSS, JavaScript, and images by default, but it can be useful for the 
# development web server to do so while you're creating your site. As a final addition to this URL mapper, you can 
# enable the serving of static files during development by appending the following lines. 
# but still need to enable file serving in production