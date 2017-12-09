from django.shortcuts import render,redirect,HttpResponse
from app import models
# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        user_obj=models.Userinfo.objects.filter(username=username,password=password).first()
        if user_obj:
            request.session["user"]={"user":username,"id":user_obj.id,"is_super":user_obj.is_super}
            return redirect("/conference/")
        else:
            error = "<script>swal('用户名或密码错误！','','error')</script>"

            return render(request,"login.html",locals())
def conference(request):
    if request.method=="GET":
        conference_list=models.Confernce.objects.all()
        return render(request,"conference_all.html",{"conference_list":conference_list})
def conference_detail(reques,conference_id):
    pass
def logout(request):
    del request.session["user"]
    return redirect("/login/")
from django.forms import Form
from django.forms import fields
from django.forms import widgets
class ConferenceForm(Form):
    title=fields.CharField(
        required=True,
        error_messages={"required":"不能为空！"},
        widget=widgets.TextInput(attrs={"class":"form-control"})
    )
    position = fields.CharField(
        required=True,
        error_messages={"required": "不能为空！"},
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )
    nunm=fields.IntegerField(
        required=True,
        error_messages={"required": "不能为空！"},
        widget=widgets.NumberInput(attrs={"class": "form-control"})
    )

def add_conference(request):
    if request.method=="GET":
        form=ConferenceForm()
        return render(request,"add_container.html",{"form":form})
    else:
        form=ConferenceForm(request.POST)
        if form.is_valid():
            models.Confernce.objects.create(**form.cleaned_data)
            return redirect("/conference/")
        else:
            return render(request, "add_container.html", {"form": form})
def edit_conference(request,conference_id):
    if request.method=='GET':
        conference_obj=models.Confernce.objects.filter(id=conference_id).first()
        form=ConferenceForm(initial={
            "title":conference_obj.title,"position":conference_obj.position,"nunm":conference_obj.nunm
        })
        return render(request,"add_container.html",{"form":form})
    else:
        form = ConferenceForm(request.POST)
        if form.is_valid():
            models.Confernce.objects.filter(id=conference_id).update(**form.cleaned_data)
            return redirect("/conference/")
        else:
            return render(request, "add_container.html", {"form": form})
def del_conference(request,conference_id):
    models.Confernce.objects.filter(id=conference_id).delete()
    return redirect("/conference/")
