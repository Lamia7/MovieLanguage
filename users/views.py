from django.shortcuts import render, redirect
from django.contrib import messages

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
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Votre compte a été créé avec succès.\n"
                f"Vous pouvez vous connecter sur le compte : {username}.",
            )

            return redirect("quizz:home")
    else:
        form = UserRegisterForm()
    # form as a context to be used in template
    return render(request, "users/register.html", {"form": form})
