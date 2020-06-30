from django.shortcuts import render


# /user/
def index(request):
    return render(request, 'index.html')