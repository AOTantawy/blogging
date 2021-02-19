from django.http import HttpResponse
from django.contrib.auth.models import User


def register(request):
    """
        Purpose: add new user to the system and authenticate him
    """
    if request.method == 'POST':
        userName = request['userName']
        password = request['password']
        try:
            User.objects.create_user(username=userName, password=password)
        except:
            return HttpResponse('Can not register this user')
        else:
            return HttpResponse('Render login page') # render login page with error message

    # else if get method
    return HttpResponse('get register page')


def login(request):
    pass


def logout(request):
    pass
