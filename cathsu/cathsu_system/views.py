from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html' )

def add_member(request):
    return render(request, 'add_member.html' )

def all_members(request):
    return render(request, 'all_members.html' )

def executive(request):
    return render(request, 'executive.html' )

def document(request):
    return render(request, 'document.html' )

def attendance(request):
    return render(request, 'attendance.html' )

def finance(request):
    return render(request, 'finance.html' )