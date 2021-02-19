from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    """
        Purpose: add new user to the system and authenticate him
    """
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        try:
            User.objects.create_user(username=userName, password=password)
        except:
            return HttpResponse('Can not register this user')
        else:
            # render login page with error message
            return HttpResponse('Render login page')

    # else if get method
    return HttpResponse('get register page')


def loginUser(request):
    """
        Purpose: authenticate user if found
    """
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        user = authenticate(request, username=userName, password=password)
        if not user:
            return HttpResponse('render login page')  # send error message

        # else if
        login(request, user)
        return HttpResponse('render home page')

    # else if method is GET
    return HttpResponse('Render login page')


def logoutUser(request):
    logout(request)
    return HttpResponse('render login page')
