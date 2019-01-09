from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.forms import UserCreationForm
from hotels.forms import SignUpForm, HotelForm
from hotels.models import hotel

# Create your views here.

from .models import hotel

from .models import hotel_rooms

from .models import hotel_photos

from .models import single_room

from .models import suit_room

from .models import vip_room

from .models import review

from .models import near_places

from .models import person

from .models import user

def elmas(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            user = authenticate(request,username=username,password = password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

    #return render(request,'signup.html',{})




def seda(request):
    return render(request, 'main_page.html', {})


def login(request):
    return render(request,'login.html')

@login_required
def logout(request):
    return  render(request,'logged_out.html',{})

def check(request):
    return  render(request,'reservation.html',{})


def hotel_detail(request, pk):
    hotels = get_object_or_404(hotel, pk=pk)
    return render(request, 'hotels/hotels_detail.html', {'hotels': hotels})


@login_required
def new_hotel(request):
    if request.method == "POST":
        hotelForm = HotelForm(request.POST)
        if HotelForm.is_valid():
            hotels = hotelForm.save(commit=False)
            hotels.save()
            return redirect('hotel_detail', pk=hotels.pk)
    else:
        hotelForm = HotelForm()
    return render(request, 'hotels/hotels_edit.html', {'hotelForm': hotelForm})