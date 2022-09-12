from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login
from django.contrib import messages
from users.forms import UserProfileForm, UserForm
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def home(request):
    return render(request, 'blog/post_list.html')


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect("blog:list")


# def register(request):
#     form_user = UserForm()
#     form_profile = UserProfileForm()
#     if request.method == 'POST':
#         form_user = UserForm(request.POST)
#         form_profile = UserProfileForm(request.POST, request.FILES)
#         if form_user.is_valid() and form_profile.is_valid():
#             user = form_user.save()
#             # form_profile.save()
#             profile = form_profile.save(commit=False)
#             profile.user = user
#             profile.save()
#             login(request, user)
#             return redirect("home")

#     context = {
#         'form_profile' : form_profile,
#         'form_user' : form_user
#     }
#     return render(request, 'users/register.html', context)

def register(request):
    form_user = UserForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            login(request, user)
            return redirect("blog:list")

    return render(request, 'users/register.html', {'form_user' : form_user})



def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("blog:list")

    return render(request, "users/user_login.html", {'form' : form})


def profile(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            # form_profile.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect("blog:list")

    context = {
        'form_profile' : form_profile,
        'form_user' : form_user
    }
    return render(request, 'users/profile.html', context)
