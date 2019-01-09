from django.shortcuts import render

# Create your views here.


#for SignUp page
#from django.contrib.auth.forms import UserCreationForm
def signup_view(request):
  #  form = UserCreationForm()
    return render(request, 'accounts/../hotels/templates/hotels/signup.html')