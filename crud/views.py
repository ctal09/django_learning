from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from crud.forms import UserDetailForm
from .models import UserInfo

# Create your views here.
def users_list(request):
    users = UserInfo.objects.all()
    context= {
        'users': users
    }
    return render(request, 'crud/list.html', context)

def user_detail(request, id):
    if request.method == "GET":
        user_instance = UserInfo.objects.get(id=id)
        print(user_instance.dob)
        formatted_date = user_instance.dob.strftime("%Y-%m-%d")
        user_instance.dob = formatted_date
        print(user_instance.dob)
        context= {
            "user_data" : user_instance,
            "form": UserDetailForm
        }
        return render(request, 'crud/detail_user.html', context)
    else:
        userobj = UserInfo.objects.get(id=id)
        userobj.first_name = request.POST.get('first_name')
        userobj.last_name = request.POST.get('last_name')
        userobj.email = request.POST.get('email')
        userobj.bio = request.POST.get('bio')
        userobj.dob = request.POST.get('dob')
        if 'profile_picture' in request.FILES:
            userobj.profile_picture = request.FILES['profile_picture']
        if not request.FILES.get('profile_picture'):
            userobj.profile_picture = userobj.profile_picture
        userobj.save()
        return redirect('/users')
    
def add_user(request):
    if request.method=="GET":
        context ={
            "form": UserDetailForm
        }
        return render(request,'crud/adduser.html', context)
    else:
        userobj = UserInfo()
        userobj.first_name = request.POST.get('first_name')
        userobj.last_name = request.POST.get('last_name')
        userobj.email = request.POST.get('email')
        userobj.bio = request.POST.get('bio')
        userobj.dob = request.POST.get('dob')
        if 'profile_picture' in request.FILES:
            userobj.profile_picture = request.FILES['profile_picture']
     
        userobj.save()
        return redirect('/users')
@csrf_exempt 
def delete_user(request, id):
    if request.method=="DELETE":
        obj = UserInfo.objects.get(id=id)
        obj.delete()
        return HttpResponse("USer Deleted Successfully")      
    else:
        return HttpResponse("Something Error Occured")