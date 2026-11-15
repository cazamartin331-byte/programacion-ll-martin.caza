from django.contrib.auth.views import LoginView, LogoutView


class MenuLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class MenuLogoutView(LogoutView):
    template_name = 'registration/logout.html'
