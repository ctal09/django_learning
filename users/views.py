from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserProfileForm
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
    return render(request, 'userform.html', {'form': form})


def send(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # form.save()  # Uncomment if you're saving to DB
            return JsonResponse({'message': 'Form submitted successfully!'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    else:
        form = UserProfileForm()
        return render(request, 'users/userform.html', {'form': form})