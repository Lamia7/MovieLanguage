from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    """Displays the registration page

    Args:
        request (obj): Django object to generate response

    Returns:
        str: Template file
    """

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("users:login")
        # If unvalid, empty form
        else:
            form = UserRegisterForm()
    else:
        form = UserRegisterForm()
    # form as a context to be used in template
    return render(request, "users/register.html", {"form": form})


@login_required  # only allows this page to logged_in users
def account(request):
    """Displays the account page when a user is logged in

    Args:
        request (obj): Django object to generate response

    Returns:
        str: Template file
    """
    return render(request, "users/account.html")
