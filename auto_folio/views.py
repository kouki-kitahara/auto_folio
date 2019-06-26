from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all().order_by('id')
    return render(request, 'users/index.html', {'users': users})

def user_show(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/show.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
        return render(request, 'users/new.html', {'form': form})
