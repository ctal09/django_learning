from django.shortcuts import render

# Create your views here.
def users_list(request):
    return render(request, 'crud/list.html')