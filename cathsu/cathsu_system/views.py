from django.shortcuts import render
from .models import Member

# Create your views here.
def login(request):
    return render(request, 'login.html' )

def add_member(request):
    return render(request, 'add_member.html' )

def all_members(request):
    members = Member.objects.all()
    context = {
        'members' : members
    }
    return render(request, 'all_members.html', context )

def executive(request):
    return render(request, 'executive.html' )

def document(request):
    return render(request, 'document.html' )

def attendance(request):
    return render(request, 'attendance.html' )

def finance(request):
    return render(request, 'finance.html' )


def dashboard(request):
    return render(request, 'dashboard.html' )




def test(request):
    if request.method == 'POST':
        member = Member()
        member.first_name = request.POST.get('form_first')
        member.last_name = request.POST.get('form_last')
        # print(request.FILES.get('form_picture'))
        member.picture = request.FILES.get('form_picture')
        member.save()
    return render(request, 'test.html')