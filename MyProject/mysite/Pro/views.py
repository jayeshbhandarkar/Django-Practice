from django.shortcuts import render, HttpResponse, redirect
from Pro.models import Contact
from Pro.models import TeamMember
from .forms import MusicianForm, AlbumForm
from .models import Musician, Album

# Create your views here.
def index(request):
    team_members = TeamMember.objects.all()
    return render(request, 'index.html', {'team_members': team_members})

def customerDataSave(request):
    if request.method=='POST':
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']
        customer_subject = request.POST['customer_subject']
        customer_message = request.POST['customer_message']

        obj = Contact(customerName=customer_name, customerEmail=customer_email, customerSubject=customer_subject, customerMessage=customer_message)
        obj.save()

        return HttpResponse('Data Save Successfully')
    return render(request, 'index.html')

def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form': form})

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})