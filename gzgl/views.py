from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from gzgl.models import *
from django.shortcuts import redirect
from django.urls import reverse



# Create your views here.
def login(request):
    if request.method=='POST':
        request.session
        uname=request.POST.get('username')
        upasswd=request.POST.get('password')
        try:
            userinfo=users.objects.get(uname=uname)
        except:
            return  render(request,'loginerr.html')
        if userinfo.upasswd==upasswd:
            request.session['uname']=userinfo.name
            return HttpResponseRedirect('/')
        else:
            return render(request,'loginerr.html')
    else:
        return render(request,'login.html')


def home(request):
    if  'uname' in request.session:
        return render(request,'index.html')
    else:return render(request,'login.html')

def  zcrk(request):
    if 'uname' not in request.session:
        return redirect('/')
    return render(request,'zcglzcrk.html')

def zcbf(request):
    pass
def zcwx(request):
    pass
def zcxw(request):
    pass
def zcjc(request):
    pass
def zcgh(request):
    pass
def jhjl(request):
    pass
def wxjl(request):
    pass
def rkjl(request):
    pass
def bfjl(request):
    pass
def xgmm(request):
    pass
def qxgl(request):
    pass
def zjgl(request):
    pass
def logout(request):
    if 'uname' not in request.session:
        return redirect('/')
    else:
        request.session.flush()
        return redirect('/')









