from django.shortcuts import render, redirect

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

            return redirect("quizz:home")
        # If unvalid, empty form
        else:
            form = UserRegisterForm()
    else:
        form = UserRegisterForm()
    # form as a context to be used in template
    return render(request, "users/register.html", {"form": form})
