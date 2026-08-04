def user_role(request):
    role = ''
    try:
        if request.user.is_authenticated:
            role = request.user.profile.role
    except Exception:
        role = ''

    return {
        'user_role': role,
        'is_admin': role == 'ADMIN',
        'is_consultant': role == 'CONSULTANT',
    }
