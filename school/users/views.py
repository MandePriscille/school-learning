from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginView(View):
    template_names = 'auth/login.html'
   
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
    #    context[""] = 
       return context
   
    
def test(request):
    return render(request, 'auth/test.html')