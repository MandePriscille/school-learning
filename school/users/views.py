from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, ProfileForm

# # Create your views here.
# class LoginView(View):
#     template_names = 'auth/login.html'
   
#     def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#     #    context[""] = 
#        return context
   
    
# def test(request):
#     return render(request, 'auth/test.html')


def acceuil(request):
   return render(request, 'index.html')


def user_register(request):
   registered =False
   if request.method == "POST":
      user_form = UserForm(data=request.POST)
      profile_form = ProfileForm(data=request.POST)
      if user_form.is_valid and profile_form.is_valid:
         user = user_form.save()
         user.save()
         
         profile = profile_form.save(commit=False)
         profile.user = user
         profile.save()
         registered=True
         return redirect('login')
      else:
         print(user_form.errors, profile_form.errors)
   else:
      user_form = UserForm()
      profile_form = ProfileForm()

   content= {
      'registered':registered,
      'form1':user_form,
      'form2':profile_form,
   }

   return render(request, 'auth/register.html', content)
   


def user_login(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(username=username, password=password)

      if user:
         if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
         else:
            HttpResponse("L'utilisateur est desactive")
      else:
         HttpResponse("Soit votre nom ou votre mot de passe est incorrect")

   else:
      return render(request, "auth/login.html")

@login_required
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/')
