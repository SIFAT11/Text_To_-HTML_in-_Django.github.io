from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm  # Update the import
from .models import Text  # Update the import

def BASE(request):
    form = PostForm()
    return render(request, 'BASE.html', {'form': form})
