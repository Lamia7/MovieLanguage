from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView

from .forms import UserRegisterForm


class RegisterView(View):
    """Displays the register page using the Class Based View: View"""
    form = UserRegisterForm()

    def get(self, request, *args, **kwargs):
        return render(request, "users/register.html", {"form": self.form})

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            self.form.save()
        return redirect("users:login")


@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    """Displays the account page when a user is logged in
    using the CBV: TemplateView """
    template_name = 'users/account.html'
