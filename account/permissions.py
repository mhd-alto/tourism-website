from functools import wraps
from django.http import HttpResponse

# from django.http import Http404
# from enum import Enum

# class Managers(Enum):
#     admin = 'Administrator'
#     manager = 'Manager'

# def check_user_able_to_see_page(*groups):

#     def decorator(function):
#         def wrapper(request, *args, **kwargs):
#             if request.user.groups.filter(
#                 name__in=[group.name for group in groups]
#             ).exists():
#                 return function(request, *args, **kwargs)
#             raise Http404

#         return wrapper

#     return decorator

def groups_only(*groups):
    def inner(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            print(request.user.groups)
            if request.user.groups.filter(name__in=groups).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return inner

