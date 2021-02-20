from django.http import HttpResponse
from django.core.paginator import Paginator
from ..models import Blog


def getBlogsCurrentPage(pageNumber):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 20)
    return paginator.get_page(pageNumber)


def index(request, pageNumber):
    """
        Purpose: view all blogs from database
    """
    # check if the user is authenticated
    # paginate page by 20 object
    if not request.user.is_authenticated:
        return HttpResponse('render login page')

    # else user is authenticated
    currentBlogs = getBlogsCurrentPage(pageNumber)
    # render index template with current blogs
    return HttpResponse('Hello from blog views')
