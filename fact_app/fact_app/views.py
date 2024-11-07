from django.shortcuts import render  # type: ignore

def home(request, *args, **kwargs):
    return render(request, 'base.html')