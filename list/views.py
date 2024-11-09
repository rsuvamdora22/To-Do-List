from django.shortcuts import render,redirect

from . models import Do,ToDo,User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def main(request):

    data = request.user
    display = None
    try:
        if request.user.is_authenticated:
            display = Do.objects.filter(user = request.user)
    except:
        None

    if request.method == 'POST':
        Title = request.POST.get('title')
        Description = request.POST.get('descp')
        Do.objects.create(Title=Title,Description=Description,user=data)
        return redirect('list')

    context = {
        'data':data,
        'display':display
    }

    return render(request,'main.html',context)

@login_required(login_url='login')
def list(request):
    data = None

    if request.method == 'POST':
        # Get the search term, or default to an empty string if 'search' is None
        Search = request.POST.get('search', '')
        
        # Filter by title and user; empty search string will match all titles
        data = Do.objects.filter(user=request.user, Title__icontains=Search)
    else:
        # If it's a GET request, display all items for the user, ordered by '-id'
        data = Do.objects.filter(user=request.user).order_by('-id')

    context = {
        'data': data
    }

    return render(request, 'list.html', context)

@login_required(login_url='login')
def detail(request,pk):

    data = Do.objects.get(id = pk)
    if request.method == 'POST' and 'remove' in request.POST:
        ToDo.objects.create(Title = data.Title, Description = data.Description, user=request.user)
        data.delete()
        return redirect('history')
    if request.method == 'POST' and 'edit3' in request.POST:
        return redirect('edit',pk=pk)
    context = {
        'data1' : data
    }

    return render(request,'details.html',context)

@login_required(login_url='login')
def edit(request,pk):
    data = Do.objects.get(id = pk)
    if request.method == 'POST':
        Title = request.POST.get('title')
        Description = request.POST.get('descp')
        data.Title = Title
        data.Description = Description
        data.save()
        return redirect('list')
    context = {
        'data2' : data
    }
    return render(request,'edit.html',context)

@login_required(login_url='login')
def history(request):
    if request.method == 'POST' and 'delete' in request.POST:
        ToDo.objects.filter(user=request.user).delete()
        return redirect('history')
    data = ToDo.objects.filter(user=request.user)
    context = {
        'data3' : data
    }

    return render(request,'history.html',context)

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

