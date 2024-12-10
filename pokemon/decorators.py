from django.shortcuts import redirect

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_role') == 'Admin':  # Asegúrate de que el rol se guarda como 'Admin'
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper


def visitor_allowed(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('usuario_rol') in ['Admin', 'Visitante']:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
