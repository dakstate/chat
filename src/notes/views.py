from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.db import models



# Create your views here.
def index(request):
    return render(request, 'notes/note.html')

def notes_show(request):
    """Выводит список заметок."""
    note = Note.objects.filter(owner=request.user).order_by('date_added')
    # context = {'topics': topics}
    return render(request, 'notes/note.html', context)
