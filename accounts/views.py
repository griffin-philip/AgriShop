from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, FarmerProfileForm, CustomerProfileForm, LoginForm
from .models import FarmerProfile, CustomerProfile 
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create profile based on role
            if user.role == 'FARMER':
                FarmerProfile.objects.create(user=user)
            else:
                CustomerProfile.objects.create(user=user)

            login(request, user)
            return redirect('complete_profile')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm


@login_required
def complete_profile(request):
    if request.user.role == "FARMER":
        profile = request.user.farmerprofile
        form_class = FarmerProfileForm
    else:
        profile = request.user.customerprofile
        form_class = CustomerProfileForm

    if request.method == "POST":
        form = form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = form_class(instance=profile)

    return render(request, "accounts/complete_profile.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('home')