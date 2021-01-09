from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Faculty, Staff, ProjectStaff
from .forms import CreateUserForm, UpdateFacultyForm, UpdateProjectStaffForm, UpdateStaffForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


# def register_page(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)
#
#                 return redirect('login')
#
#         context = {'form': form}
#         return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def people(request):
    faculties = Faculty.objects.all()
    staffs = Staff.objects.all()
    project_staffs = ProjectStaff.objects.all()

    context = {'faculties': faculties,
               'staffs': staffs,
               'project_staffs': project_staffs}

    return render(request, 'people.html', context)


@login_required()
def profile(request):
    group = request.user.groups.all()[0].name

    if request.method == 'POST':
        if group == 'Faculty':
            p_form = UpdateFacultyForm(request.POST, instance=request.user.faculty)
        elif group == 'staff':
            p_form = UpdateStaffForm(request.POST, instance=request.user.staff)
        elif group == 'project_staff':
            p_form = UpdateProjectStaffForm(request.POST, instance=request.user.projectstaff)

        if p_form.is_valid():
            p_form.save()
            messages.info(request, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        if group == 'Faculty':
            p_form = UpdateFacultyForm(instance=request.user.faculty)
        elif group == 'staff':
            p_form = UpdateStaffForm(instance=request.user.staff)
        elif group == 'project_staff':
            p_form = UpdateProjectStaffForm(instance=request.user.projectstaff)

    context = {'form': p_form,
               'group': group}

    return render(request, 'profile.html', context)
