from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserProfileForm, FormTwo, UserModelForm
from django.core.files.storage import FileSystemStorage
# from django.views.decorators.csrf import csrf_exempt  # Optional if using CSRF correctly
# Create your views here.
def home(request):
    return HttpResponse("Hello, world! This is the home page of the users app.")

def username(request, id):
    response = HttpResponse()
    response.content = """Hello, user with ID {}!!""".format(id)
    return response

def education(request,id):
    return HttpResponse("This is the education page of the user {} app.".format(id))

def experience(request, id):
    return HttpResponse("This is the experience page of the user {} app.".format(id))

def rednder_form(request):
    form = UserProfileForm()
    if request.method=='GET':
        return render(request, 'userform.html', {'form': form})
    else:
        #post
        print(request.POST)
        user_id = request.POST.get('id_name')
        # return render(request,'formreturn.html', {'data': request.POST})
        return redirect(f'/user/{user_id}/')
        
def send(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'id_name': form.cleaned_data['id_name'],
                'email': form.cleaned_data['email']
            }
            return JsonResponse({'success': True, 'data': data})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = UserProfileForm()
        return render(request, 'users/userform.html', {'form': form})

def form2(request):
    form = FormTwo()
    if request.method == 'GET':
        return render(request, 'userform.html', {'form': form})
    else:
        form = FormTwo(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formreturn.html', {'data': form.cleaned_data})
        else:
            return render(request, 'formreturn.html', {'data': form})



def usermodelform(request):
    form = UserModelForm
    if request.method == "GET":
        return render(request, 'Usermodel.html', {'form': form})
    else:
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'responseUsermodel.html', {'data': form.cleaned_data})
        else:
            print(form.errors)
            return render(request, 'Usermodel.html', {'form': form})
def statictest(request):
    return render(request, 'static.html', {'name': 'Manisha'})

def manage_media(request):
    uploaded_files= []
    if request.method== 'POST':
        file_obj = request.FILES['file']
        fs = FileSystemStorage()
        print(file_obj.name)
        filename = fs.save(file_obj.name, file_obj)
        print("After saving the file", filename)
    return render(request, 'media.html', {'uploaded_files': uploaded_files})
    