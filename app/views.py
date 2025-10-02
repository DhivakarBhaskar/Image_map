from django.shortcuts import render
def map(request):
    return render(request, 'map.html')
def pettai(request):
    return render(request, 'pettai.html')
def ara(request):
    return render(request, 'ara.html')
def lake(request):
    return render(request, 'lake.html')
def raja(request):
    return render(request, 'raja.html')
def heaven(request):
    return render(request, 'heaven.html')

# Add more views as needed
