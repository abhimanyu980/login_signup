from django.shortcuts import render, get_object_or_404
from .models import History
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



@login_required
def home(request):
    context = {
        'historys': History.objects.all()
    }
    return render(request, 'history/home.html', context)

@login_required
def delete(request, id):
    history = History.objects.get(id=id)
    history.delete()
    return redirect('history')


