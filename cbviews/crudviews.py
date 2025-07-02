from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import UserDetailForm
from .models import UserInfo

class DetailUser(DetailView):
    model = UserInfo
    template_name = 'detail_user.html'
    context_object_name = 'user_data'
    
class UpdateUser(UpdateView):
    form_class=UserDetailForm
    template_name='updateuser.html'
    context_object_name='user_data'
    model = UserInfo
    success_url ='/c/users'


class Adduser(CreateView):
    form_class = UserDetailForm
    model= UserInfo
    template_name ='adduser.html'
    success_url ='/c/users'
    
class DeleteUser(DeleteView): 
        model = UserInfo
        template_name = 'delet.html'
        success_url ='/c/users'
     
        


class ListUser(ListView):
    template_name='list.html' 
    model = UserInfo
    context_object_name = 'data'
    
    
    
    
   