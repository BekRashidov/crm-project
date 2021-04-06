from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from leads.views import landing_page, LandingPageView, SignupView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('leads/', include("leads.urls", namespace="leads")),
    path('agents/', include("agents.urls", namespace="agents")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

