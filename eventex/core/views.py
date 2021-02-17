from django.shortcuts import render

# Create your views here.
# View inicial  2
def home(request):
    return render(request, 'index.html')
