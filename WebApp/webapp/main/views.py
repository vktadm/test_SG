from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
import logging

from .prepare_data import get_user_receptions

@login_required
def index(request):
    """Выводит записи пациентв."""
    reseptions = get_user_receptions(request.user)
    context = {'reseptions': reseptions}
    return render(request, 'index.html', context)

def user_login(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")
        if form.is_valid():
            logging.info(f"Вход в ЛК: {request.POST['username']}")
            user = form.get_user()
            login(request, user)
            return redirect('index')
        logging.info(f"Попытка войти в ЛК: {request.POST['username']}")
    context = {'form': form}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return render(request, 'logged_out.html')