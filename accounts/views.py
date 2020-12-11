from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, noteForm, EditUserChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import note
from django.contrib import messages

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'accounts/home.html', {'form': form})
    else :
        return HttpResponseRedirect('/dashboard/')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/dashboard/')         
    else :
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_notes(request):
    if request.user.is_authenticated:
        user = request.user
        data = note.objects.filter(user=user)[:5]
        return render(request, 'accounts/notes.html', {'data': data})
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def take_notes(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            takenotes = request.POST['takenotes']
            new = note(title=title, takenotes=takenotes, user=request.user)
            new.save()
            messages.success(request, 'succesfully saved!')
            return HttpResponseRedirect('/dashboard/')
        else:
            form = noteForm()
            return render(request, 'accounts/takenotes.html', {'form': form})
    else:
        return HttpResponseRedirect('/')

def your_notes(request):
    if request.user.is_authenticated:
        user = request.user
        data = note.objects.filter(user=user)
        return render(request, 'accounts/yournotes.html', {'data': data})
    else:
        return HttpResponseRedirect('/')

def user_setting(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Updated Successfully!!')
                form.save()
        else:
            form = EditUserChangeForm(instance=request.user)
        return render(request, 'accounts/setting.html', {'name': request.user.get_full_name(), 'form': form})
    else:
        return HttpResponseRedirect('/')

def data_delete(request, pk):
    deldata = note.objects.get(id=pk)
    deldata.delete()
    return HttpResponseRedirect('/dashboard/')

def data_update(request, pk):
    updatedata = note.objects.get(id=pk)
    forms = noteForm(instance=updatedata)
    if request.method == 'POST':
        forms = noteForm(request.POST, instance=updatedata)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/dashboard/')
    return render(request, 'accounts/update.html', {'forms': forms})

def data_views(request, pk):
    forms = note.objects.get(id=pk)
    return render(request, 'accounts/view.html', {'forms': forms})
