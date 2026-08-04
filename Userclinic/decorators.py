from django.shortcuts import redirect
from .models import Profile


def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        if request.user.is_superuser:
            return view_func(
                request,
                *args,
                **kwargs
            )

        try:
            role = request.user.profile.role
        except Profile.DoesNotExist:
            role = None
        except Exception:
            role = None

        if role != 'ADMIN':
            return redirect('login')

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper