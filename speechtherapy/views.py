from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def start_therapy(request):
    sentences = [
        "नमस्ते, आप कैसे हैं?",
        "मुझे पानी चाहिए।",
        "क्या आप मेरी मदद कर सकते हैं?",
        "यह एक सुंदर दिन है।"
    ]
    return render(request, 'start_therapy.html', {'sentences': sentences})