from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "Main/main.html")

def author(request):
    return render(request, "Author/main.html")

def book(request):
    return render(request, "Book/main.html")