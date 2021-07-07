from django.shortcuts import render


# Create your views here.
def register(request):
    """Displays the registration page

    Args:
        request (obj): Django object to generate response

    Returns:
        str: Template file
    """
    return render(request, "users/register.html")
