from django.shortcuts import render

# Create your views here.
# View inicial
def home(request):
    return render(request, 'index.html')
