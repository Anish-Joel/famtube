
# Create your views here.
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import (CreateView,FormView)
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm, RegisterForm

User = get_user_model()

#def register_view(request):
   # form = RegisterForm(request.POST or None)
  #  if form.is_valid():
       # passkey = form.cleaned_data.get("passkey")
       
      #  try:
       #     user = User.objects.create_user(passkey)
       # except:
      # 3     user = None
        #if user != None:
            #login(request, user)
           # return redirect("/")
       # else:
           # request.session['register_error'] = 1 # 1 == True
  #  return render(request, "sa.html", {"form": form})


#def login_view(request):
  #  form = LoginForm(request.POST or None)
  #  if form.is_valid():
    #   passkey = form.cleaned_data.get("passkey")
        
      #  user = authenticate(request, passkey=passkey)
      #  if user != None:
            # user is valid and active -> is_active
         #   # request.user == user
          #  login(request, user)
         #   return redirect("/")
       # else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
       #   e  request.session['invalid_user'] = 1 # 1 == True
    #return render(request, "registration/login.html", {"form": form})

#class register_view(CreateView):
  #  form_class = RegisterForm
  #  success_url ='/login/'
  #  template_name ='sa.html'

class login_view(FormView):
    form_class = LoginForm
    success_url ='/'
    
    template_name ='registration/login.html'
    
    def form_valid(self,form):
        request = self.request
        next_  =request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or redirect('/')
        username =form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username =username,password = password)
        if user is not None:
            login(request,user)
     
        return super(login_view,self).form_invalid(form)
def register_view(request):
    form = RegisterForm(request.POST or None)
    context ={"form":form}
    if form.is_valid():
        form.save()
    return render(request,"sa.html",context)    
