from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def start_therapy(request):
    return render(request, 'start_therapy.html',)